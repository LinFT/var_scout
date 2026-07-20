from var_scout.reporters.base import BaseReporter

class ShapeReporter(BaseReporter):
  def report(self, func_name, local_vars, is_crash=False, error=None):
    if is_crash:
      status = f"Exception Report ({type(error).__name__} - {error})"
    else:
      status = "Normal Execution Report"
    print(f"\n>> Function: {func_name} | {status}")
      
    if not local_vars:
        print("  (No local variable found)")
    
    for name, value in local_vars.items():
        if name.startswith('__'):
            continue
            
        shape = getattr(value, 'shape', None)
        if shape is not None:
            print(f"  Variable '{name}': shape={shape}")
        else:
            print(f"  Variable '{name}': shape=None (dtype: {type(value).__name__})")
    print("=" * 60)
