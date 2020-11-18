# Releasing flake8-assert-msg

```diff
--- a/README.md
+++ b/README.md
@@ -27,7 +27,7 @@ Sample `.pre-commit-config.yaml`:
     rev: 3.8.1
     hooks:
     -   id: flake8
-        additional_dependencies: [flake8-assert-msg==1.0.0]
+        additional_dependencies: [flake8-assert-msg==1.1.0]

--- a/src/flake8_assert_msg/version.py
+++ b/src/flake8_assert_msg/version.py
@@ -1 +1 @@
-VERSION = (1, 0, 0)
+VERSION = (1, 1, 0)
```
