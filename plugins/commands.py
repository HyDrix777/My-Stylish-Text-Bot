import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant




force_subhydra = "songdownload_group"



@Client.on_message(filters.command('start'))
async def start(c, m):
    if force_subhydra:
        try:
            user = await c. get_chat_member(force_subhydra, m.from_user.id)
            if user.status == "kick out":
                await m.reply_text("you are banned")
                return
        except UserNotParticipant:
            await m.reply_text(
                text=f"Êá´Ê {m.from_user.first_name} ðYá´á´ á´Êá´ É´á´á´ á´á´ÉªÉ´á´á´ á´Ê É¢Êá´á´á´.\n\nÒÉªÊsá´ á´á´ÉªÉ´ á´á´ á´Ê É¢Êá´á´á´ á´Êá´É´ á´ÊÉªá´á´ sá´á´Êá´ Êá´á´á´á´É´ Êá´Êá´á´¡ ðâ¤ï¸",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Join My Group", url=f"t.me/{force_subhydra}")
                 ],[
                 InlineKeyboardButton("Click start Botton", url="https://t.me/StylishText_X_Bot?start")
                 ]]
                )
            )
            return
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'zautebot'

    # start text
    text = f"""ð Êá´Ê! {m.from_user.mention(style='md')},

ââââââââââââââââ
ââââââ¦ââââââââââ
ââââââ©ââââââââââ
ââââââââââââââââ
**[âï¸](https://telegra.ph/file/648381c22575438a193b9.jpg) Éª á´á´ sá´ÊÊÉªsÊ á´á´xá´ Êá´á´ **

**I á´á´É´ Êá´Êá´ Êá´á´ á´á´ ÒÉªÉ´á´ sá´ÊÊÉªsÊ Òá´É´á´s. á´á´sá´ sá´É´á´ á´á´ Êá´á´Ê á´á´xá´.**
**Éª Êá´á´ á´ É´á´á´¡ sá´ÊÊá´ á´á´xá´s É¢á´ á´É´á´ á´Êá´á´á´ Éªá´ á´á´á´** ð

ð¨âð»**Bá´á´ Dá´á´ á´Êá´á´á´Ê:** [Click](https://github.com/Ns-Bots)
ð¶ââï¸**Má´ÉªÉ´á´á´ÉªÉ´á´á´ ÊÊ:** [Hydrix](https://t.me/HydraLivegrambot)
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('ð¥ MÊ É¢Êá´á´á´', url=f"https://t.me/songdownload_group"),
            InlineKeyboardButton('ð¢ á´Êá´É´É´á´Ê', url=f"https://t.me/Tg_Galaxy")
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    if force_subhydra:
        try:
            user = await c. get_chat_member(force_subhydra, m.from_user.id)
            if user.status == "kick out":
                await m.reply_text("you are banned")
                return
        except UserNotParticipant:
            await m.reply_text(
                text=f"Êá´Ê {m.from_user.first_name} ðYá´á´ á´Êá´ É´á´á´ á´á´ÉªÉ´á´á´ á´Ê É¢Êá´á´á´.\n\nÒÉªÊsá´ á´á´ÉªÉ´ á´á´ á´Ê É¢Êá´á´á´ á´Êá´É´ á´ÊÉªá´á´ sá´á´Êá´ Êá´á´á´á´É´ Êá´Êá´á´¡ ðâ¤ï¸",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Join My Group", url=f"t.me/{force_subhydra}")
                 ],[
                 InlineKeyboardButton("Click start Botton", url="https://t.me/StylishText_X_Bot?start")
                 ]]
                )
            )
            return
    buttons = [[
        InlineKeyboardButton('ðð¢ððð ððððð', callback_data='style+typewriter'),
        InlineKeyboardButton('ðð¦ð¥ðððð', callback_data='style+outline'),
        InlineKeyboardButton('ððð«ð¢ð', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('ðºðððð', callback_data='style+bold_cool'),
        InlineKeyboardButton('ððððð', callback_data='style+cool'),
        InlineKeyboardButton('Sá´á´ÊÊ Cá´á´s', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('ðð¸ðð¾ðð', callback_data='style+script'),
        InlineKeyboardButton('ð¼ð¬ð»ð²ð¹ð½', callback_data='style+script_bolt'),
        InlineKeyboardButton('áµâ±â¿Ê¸', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('áOá°Iá', callback_data='style+comic'),
        InlineKeyboardButton('ð¦ð®ð»ð', callback_data='style+sans'),
        InlineKeyboardButton('ððð£ð¨', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('ðð¢ð¯ð´', callback_data='style+slant'),
        InlineKeyboardButton('ð²ðºðð', callback_data='style+sim'),
         InlineKeyboardButton('â¸ï¸â¾ï¸âï¸â¸ï¸âï¸âºï¸âï¸', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('ðï¸ðï¸ð¡ï¸ðï¸ðï¸ðï¸ð¢ï¸', callback_data='style+circle_dark'),
        InlineKeyboardButton('ðð¬ð±ð¥ð¦ð ', callback_data='style+gothic'),
        InlineKeyboardButton('ð²ððððð', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('ð§ã½ð¾ð·â¹', callback_data='style+cloud'),
        InlineKeyboardButton('êµdsá´d', callback_data='style+happy'),
        InlineKeyboardButton('á°iá¶áá', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('É´á´xá´ ãã', callback_data="nxt"),
        InlineKeyboardButton("ð¥ á´Ê É¢Êá´á´á´", url="https://t.me/Music_Galaxy_Dl")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('ð¸âðµâðªâð¨âð®âð¦âð±â', callback_data='style+special'),
            InlineKeyboardButton('ðððð°ðð´ð', callback_data='style+squares'),
            InlineKeyboardButton('ðï¸ðï¸ðï¸ð°ï¸ðï¸ð´ï¸ðï¸', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('êªêªá¦êªêª¶êªá¥´ð²êª', callback_data='style+andalucia'),
            InlineKeyboardButton('çªåå áå', callback_data='style+manga'),
            InlineKeyboardButton('ä¸ï½²ï¾åãºï¾', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('ÕÔ¹ÉÉ¾ÔµÉ', callback_data='style+bubbles'),
            InlineKeyboardButton('UÍnÍdÍeÍrÍlÍiÍnÍeÍ', callback_data='style+underline'),
            InlineKeyboardButton('êêê·ê©êêê', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('RÒaÒyÒsÒ', callback_data='style+rays'),
            InlineKeyboardButton('BÒiÒrÒdÒsÒ', callback_data='style+birds'),
            InlineKeyboardButton('SÌ¸lÌ¸aÌ¸sÌ¸hÌ¸', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('sâ tâ oâ pâ ', callback_data='style+stop'),
            InlineKeyboardButton('ÐÐ¼ÑÑÐ¾', callback_data='style+skyline'),
            InlineKeyboardButton('AÍrÍrÍoÍwÍsÍ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('áªáá­á¿á', callback_data='style+qvnes'),
            InlineKeyboardButton('SÌ¶tÌ¶rÌ¶iÌ¶kÌ¶eÌ¶', callback_data='style+strike'),
            InlineKeyboardButton('ÆÑÏz', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('ãã Êá´á´á´', callback_data='nxt+0'),
            InlineKeyboardButton("ð¥ á´Ê É¢Êá´á´á´", url="https://t.me/Music_Galaxy_Dl"),
            InlineKeyboardButton('next', callback_data='nxt2')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass
