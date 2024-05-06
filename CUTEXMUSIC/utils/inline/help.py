from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from CUTEXMUSIC import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="THREEPAGE",
        ),
        InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
        InlineKeyboardButton(
            text=_["NEXT_BUTTON"], 
            callback_data="SECONDPAGE",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
    
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="help_callback hb12",
                ),
            ],
           [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="help_callback hb13",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="help_callback hb14",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="help_callback hb15",
                ),
           ],
            [
                InlineKeyboardButton(
                    text=_["H_B_16"],
                    callback_data="help_callback hb16",
                ),
                InlineKeyboardButton(
                    text=_["H_B_17"],
                    callback_data="help_callback hb17",
                ),
    
                InlineKeyboardButton(
                    text=_["H_B_18"],
                    callback_data="help_callback hb18",
                ),
            ],
                
            mark,
        ]
    )
    return upl

def twohelp_pannel(_, START: Union[bool, int] = None):
     first = [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"close")]
     second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settings_back_helper",
        ),
         InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
        InlineKeyboardButton(
            text=_["NEXT_BUTTON"], 
            callback_data="FOURPAGE",
        ),
     ]
     mark = second if START else first
     upl = InlineKeyboardMarkup(
         [
         [
                InlineKeyboardButton(
                    text=_["H_B_19"],
                    callback_data="help_callback hb19",
                ),
                InlineKeyboardButton(
                    text=_["H_B_20"],
                    callback_data="help_callback hb20",
                ),
                InlineKeyboardButton(
                    text=_["H_B_21"],
                    callback_data="help_callback hb21",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_22"],
                    callback_data="help_callback hb22",
                ),
                InlineKeyboardButton(
                    text=_["H_B_23"],
                    callback_data="help_callback hb23",
                ),
                InlineKeyboardButton(
                    text=_["H_B_24"],
                    callback_data="help_callback hb24",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_25"],
                    callback_data="help_callback hb25",
                ),
                InlineKeyboardButton(
                    text=_["H_B_26"],
                    callback_data="help_callback hb26",
                ),
                InlineKeyboardButton(
                    text=_["H_B_27"],
                    callback_data="help_callback hb27",
                ),
            ],
           [
                InlineKeyboardButton(
                    text=_["H_B_28"],
                    callback_data="help_callback hb28",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_29"],
                    callback_data="help_callback hb29",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_30"],
                    callback_data="help_callback hb30",
                ),
           ],
            [
                InlineKeyboardButton(
                    text=_["H_B_31"],
                    callback_data="help_callback hb31",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_32"],
                    callback_data="help_callback hb32",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_33"],
                    callback_data="help_callback hb33",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_34"],
                    callback_data="help_callback hb34",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_35"],
                    callback_data="help_callback hb35",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_36"],
                    callback_data="help_callback hb36",
                ),
             ],
            mark,
        ]
    )
     return upl

def threehelp_pannel(_, START: Union[bool, int] = None):
     first = [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"close")]
     second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="FOURPAGE",
        ),
        InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data=f"close",
        ),
     ]
     mark = second if START else first
     upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_37"],
                    callback_data="help_callback hb37",
                ),
                InlineKeyboardButton(
                    text=_["H_B_38"],
                    callback_data="help_callback hb38",
                ),
            ],
        [
            InlineKeyboardButton(
                text=_["H_B_39"],
                callback_data="REPOSITORYKA",
            ),
        ],
     mark,
        ]
     )
     return upl  


def fourhelp_pannel(_, START: Union[bool, int] = None):
     first = [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data=f"close")]
     second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="SECONDPAGE",
        ),
         InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
        InlineKeyboardButton(
            text=_["NEXT_BUTTON"], 
            callback_data="THREEPAGE",
        ),
     ]
     mark = second if START else first
     upl = InlineKeyboardMarkup(
         [
         [
                InlineKeyboardButton(
                    text=_["H_B_40"],
                    callback_data="help_callback hb40",
                ),
                InlineKeyboardButton(
                    text=_["H_B_41"],
                    callback_data="help_callback hb41",
                ),
                InlineKeyboardButton(
                    text=_["H_B_42"],
                    callback_data="help_callback hb42",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_43"],
                    callback_data="help_callback hb43",
                ),
                InlineKeyboardButton(
                    text=_["H_B_44"],
                    callback_data="help_callback hb44",
                ),
                InlineKeyboardButton(
                    text=_["H_B_45"],
                    callback_data="help_callback hb45",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_46"],
                    callback_data="help_callback hb46",
                ),
                InlineKeyboardButton(
                    text=_["H_B_47"],
                    callback_data="help_callback hb47",
                ),
                InlineKeyboardButton(
                    text=_["H_B_48"],
                    callback_data="help_callback hb48",
                ),
            ],
           [
                InlineKeyboardButton(
                    text=_["H_B_49"],
                    callback_data="help_callback hb49",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_50"],
                    callback_data="help_callback hb50",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_51"],
                    callback_data="help_callback hb51",
                ),
           ],
            [
                InlineKeyboardButton(
                    text=_["H_B_52"],
                    callback_data="help_callback hb52",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_53"],
                    callback_data="help_callback hb53",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_54"],
                    callback_data="help_callback hb54",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_55"],
                    callback_data="help_callback hb55",
                 ),
               InlineKeyboardButton(
                    text=_["H_B_56"],
                    callback_data="help_callback hb56",
                 ),
              InlineKeyboardButton(
                    text=_["H_B_57"],
                    callback_data="help_callback hb57",
                ),
             ],
            mark,
        ]
    )
     return upl
    

def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["HOME_BUTTON"], 
                    callback_data="help_back",
        ),
                InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
            ]
        ]
    )
    return upl

def secondhelp_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="SECONDPAGE",
                ),
                InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
                InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
            ]
        ]
    )
    return upl


def threehelp_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="repo_backk",
                ),
                InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
                InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
            ]
        ]
    )
    return upl

def fourhelp_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="FOURPAGE",
                ),
                InlineKeyboardButton(
            text=_["HOME_BUTTON"], 
            callback_data="help_back",
        ),
                InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
            ]
        ]
    )
    return upl

def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
