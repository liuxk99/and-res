# and-res
android resource analysis and editing

# id-editor
public resource analysis and generate new continuous id to append original public.xml and overlay.xml
+ replace customized public.xml overlay.xml and eui-public.xml
+ run res_public_parser_test.TestResPublicParser.test_eui

# res_names_parser
it use to rename resource in client files, such as .xml .java。
+ the res_names.txt section
```
  anim.close_enter_left_to_right, anim.eui_support_close_enter_left_to_right
  anim.close_exit_left_to_right, anim.eui_support_close_exit_left_to_right
```
You must specify own res_names.txt
+ client files dir
You must specify own client files dir, often, it as below:
"...\xxx\src\main"
