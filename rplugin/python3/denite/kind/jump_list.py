# ============================================================================
# FILE: jump_list.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from .base import Base


class Kind(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'jump_list'

    def action_default(self, context):
        target = context['targets'][0]
        path = target['action__path']
        if self.vim.call('fnamemodify',
                         self.vim.current.buffer.name, ':p') != path:
            self.vim.call(
                'denite#util#execute_path', 'edit', path)
        if int(target.get('action__line', 0)) > 0:
            self.vim.current.window.cursor = (int(target['action__line']), 0)
        if int(target.get('action__col', 0)) > 0:
            self.vim.current.window.cursor = (0, int(target['action__col']))
        # Open folds
        self.vim.command('normal! zv')
