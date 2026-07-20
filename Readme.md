### 📂 Project Structure

* 📦 **`var_scout/`**
  * 📄 `__init__.py` — Export the public API
  * 📄 `decorator.py` — Core decorator implementation (`sys.settrace`)
  * 📂 **`reporters/`** — Reporting backends
    * 📄 `__init__.py`
    * 📄 `base.py` — Base reporter interface
    * 📄 `shape.py` — Shape reporter
    * 📄 `console.py` — *Console reporter (future extension)*
    * 📄 `markdown.py` — *Markdown table reporter (future extension)*
    * 📄 `file.py` — *File reporter (future extension)*
  * 📂 **`utils/`**
    * 📄 `inspector.py` — Framework-specific variable inspection utilities
