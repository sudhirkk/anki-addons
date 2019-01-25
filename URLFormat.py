
# -*- coding: utf-8 -*-
# Copyright 2013 Sudhir Krishnan <http://www.sudhirkk.com>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki.hooks import wrap
from aqt.editor import Editor
from anki.utils import json

def urlFormat(self):
        the_url = "".join(["<a href=\"",
                               self.web.selectedText(),
                               "\">", self.web.selectedText(), "</a>"])
        self.web.eval("document.execCommand('inserthtml', false, %s);"
                  % json.dumps(the_url))

def setupButtons(self):
    self._addButton("urlButton", lambda s=self: urlFormat(self),
                    text=u"L", tip="HTML (Ctrl+Shift+h", key="Ctrl+Shift+h")

Editor.urlFormat = urlFormat
Editor.setupButtons = wrap(Editor.setupButtons, setupButtons)

