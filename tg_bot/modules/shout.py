from tg_bot import application
from telegram import Update
from telegram.ext import CallbackContext
from tg_bot.modules.helper_funcs.decorators import kigcmd


@kigcmd(command="shout")
async def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = [" ".join(list(text))]
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return await update.effective_message.reply_text(msg, parse_mode="MARKDOWN")
