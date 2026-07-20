class BaseReporter:
  def report(self, func_name: str, local_vars: dict, is_crash: bool, error: Exception=None):
    raise NotImplementedError