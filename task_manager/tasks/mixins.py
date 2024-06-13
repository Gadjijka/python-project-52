from django.contrib import messages
from django.shortcuts import redirect


class PermitDeleteTaskMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().creator != request.user:
            message = 'A task can only be deleted by its user'
            messages.error(request, message)
            return redirect("tasks")
        return super().dispatch(request, *args, **kwargs)
