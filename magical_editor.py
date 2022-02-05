from time import sleep
from argparse import ArgumentParser
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import UpdateShortMessage, Message
from telethon.errors import MessageNotModifiedError
from configs.config import (
    API_ID, API_HASH, SESSION_STRING
)
from configs.config import write_session_string_in_config
from animations.tape_factory import TapeFactory
from animations.anim_setting import AnimationSetting


SEPARATOR: str = "|"
DELAY_TIME: float = 0.6
TAPE_BY_COMMAND: dict[str: AnimationSetting] = {
    "/example": AnimationSetting(TapeFactory.get_example(), 2),
    "/pulse_heart": AnimationSetting(TapeFactory.get_pulse_heart(), 3),
    "/growH": AnimationSetting(TapeFactory.get_increasing(), 1),
    "/blink": AnimationSetting(TapeFactory.get_blinking_heart(7), 1),
}

print_session_key = False
client: TelegramClient = TelegramClient(
    StringSession(SESSION_STRING), API_ID, API_HASH
)


@client.on(events.NewMessage(outgoing=True))
async def handler_new_message(event: events.NewMessage.Event) -> None:
    update: UpdateShortMessage = event.original_update
    try:
        if isinstance(event.original_update, UpdateShortMessage):
            command, text = (
                update.message.split(SEPARATOR, 1) if SEPARATOR in update.message
                else (update.message, None)
            )
            controller = TAPE_BY_COMMAND.get(command)
            if controller is not None:
                print(
                    f"id: {update.id} userId: {update.user_id}\n"
                    f"command: {command} extra text: {text}\n"
                )
                await client.get_dialogs()
                await play_animation(controller, event.message, text)
    except Exception as e:
        print(e)


async def play_animation(
        animation_setting: AnimationSetting,
        message: Message,
        text: str = None
) -> None:
    async def play(frames: list[str]) -> None:
        if len(frames) == 0:
            return
        for frame in frames:
            try:
                await message.edit(frame)
            except MessageNotModifiedError as e:
                print(f"Один из кадров был пропущен: {frame}")
                continue
            sleep(DELAY_TIME)

    tape = animation_setting.tape

    await play(tape.get_start_frames())
    for i in range(animation_setting.repeat_time):
        await play(tape.get_loop_frames())
    await play(tape.get_end_frames())

    if text is not None:
        await message.edit(text)


def process_key() -> None:
    def configure_arg_parser():
        arg_parser.add_argument("--sessionKey", "-sk", default=False,
                                action="store_true", dest="sk",
                                help="Получить ключ сессии")

    global print_session_key
    arg_parser = ArgumentParser()
    configure_arg_parser()
    args = arg_parser.parse_args()
    print_session_key = args.sk


def main() -> None:
    process_key()

    print("\U00002665 magic")
    client.start(
        password=input("If you have 2FA input password: ")
        if SESSION_STRING is None else ""
    )
    print("log in\n")
    if print_session_key:
        print(client.session.save(), end="\n\n")
    if SESSION_STRING is None:
        write_session_string_in_config(client.session.save())
    client.run_until_disconnected()


if __name__ == "__main__":
    main()
