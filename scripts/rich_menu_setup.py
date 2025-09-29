from config.line_bot_setting import CHANNEL_ACCESS_TOKEN

from rich_menu_function import RichMenu

rich_menu = RichMenu(CHANNEL_ACCESS_TOKEN)

body = {
    "size": {
        "width": 2500,
        "height": 1686
    },
    "selected": True,
    "name": "功能選單",
    "chatBarText": "功能選單",
    "areas": [
        {
            "bounds": {
                "x": 126,
                "y": 228,
                "width": 688,
                "height": 693
            },
            "action": {
                "type": "postback",
                "data": "function_selected=職能分析"
            }
        },
        {
            "bounds": {
                "x": 912,
                "y": 237,
                "width": 687,
                "height": 679
            },
            "action": {
                "type": "postback",
                "data": "function_selected=技能差距"
            }
        },
        {
            "bounds": {
                "x": 1691,
                "y": 228,
                "width": 678,
                "height": 683
            },
            "action": {
                "type": "postback",
                "data": "function_selected=推薦課程"
            }
        },
        {
            "bounds": {
                "x": 126,
                "y": 940,
                "width": 693,
                "height": 669
            },
            "action": {
                "type": "postback",
                "data": "function_selected=學習通知"
            }
        },
        {
            "bounds": {
                "x": 911,
                "y": 940,
                "width": 688,
                "height": 669
            },
            "action": {
                "type": "postback",
                "data": "function_selected=諮詢助教"
            }
        },
        {
            "bounds": {
                "x": 1694,
                "y": 945,
                "width": 684,
                "height": 673
            },
            "action": {
                "type": "uri",
                "uri": "https://skill-flow-seven.vercel.app/"
            }
        }
    ]
}
rich_menu_id = rich_menu.create_rich_menu(body)

rich_menu.attach_image(rich_menu_id, 'rich_menu_image.png')
rich_menu.set_default_rich_menu(rich_menu_id)
