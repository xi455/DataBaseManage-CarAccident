from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect


class GroupPerms(UserPassesTestMixin, LoginRequiredMixin):
    def test_func(self):
        # 判斷用戶是否擁有相應的群組權限，如果有則返回 True，否則返回 False
        has_group = self.request.user.groups.filter(name="intendant").exists() or self.request.user.is_superuser
        return has_group

    def handle_no_permission(self):
        return redirect("403")
