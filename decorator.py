def log_local_vars(reporter: BaseReporter=ShapeReporter()):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      local_vars = {}
      exception_occurred = False
      
      # Catch local variables while "return" runs in func
      def trace_calls(frame, event, arg):
        if event == 'return':
          local_vars.update(frame.f_locals)
        elif event == 'exception':
          nonlocal exception_occurred
          exception_occurred = True
          local_vars.update(frame.f_locals)
        return trace_calls
      
      # Start tracing
      sys.settrace(trace_calls)
      try:
        result = func(*args, **kwargs)
      except Exception as e:
        reporter.report(func.__name__, local_vars, is_crash=True, error=e)
        raise e
      finally:
        sys.settrace(None)
      
      if not exception_occurred:
        reporter.report(func.__name__, local_vars, is_crash=False)

      return result
    return wrapper
  return decorator