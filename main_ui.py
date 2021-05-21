from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()


class ContentNavigationDrawer(BoxLayout):
    pass
