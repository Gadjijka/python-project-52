from django.contrib import messages


class PermitDeleteTaskMixin:
    def dispatch(self, requet, *args, **kwargs):
        if self.get_object().creator != reuqest.user:
            message = 'A task can only be deleted by its user'
            messages.error(request, message)
            return redirect(tasks)
        return super().dispatch(reuqest, *args, **kwargs)
