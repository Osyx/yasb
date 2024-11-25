# Windows Desktops Widget
| Option                     | Type    | Default                  | Description                                                                 |
|----------------------------|---------|--------------------------|-----------------------------------------------------------------------------|
| `label_workspace_btn`    | string  | `'{index}'`              | The format string for workspace buttons.                                    |
| `label_workspace_active_btn` | string | `'{index}'`              | The format string for the active workspace button.                          |
| `container_padding`  | dict | `{'top': 0, 'left': 0, 'bottom': 0, 'right': 0}`      | Explicitly set padding inside widget container.

## Example Configuration

```yaml
windows_workspaces:
  type: "yasb.windows_desktops.WorkspaceWidget"
  options:
    label_workspace_btn: "\udb81\udc3d"
    label_workspace_active_btn: "\udb81\udc3e"
    container_padding: 
      top: 0
      left: 8
      bottom: 0
      right: 8
```

## Description of Options
- **label_workspace_btn:** The format string for workspace buttons, can be icon or {index}.
- **label_workspace_active_btn:** The format string for the active workspace button, can be icon or {index}.
- **container_padding:** Explicitly set padding inside widget container.


## Style
```css
.windows-desktops {} /*Style for widget.*/
.windows-desktops .widget-container {} /*Style for widget container.*/
.windows-desktops .ws-btn {} /*Style for buttons.*/
.windows-desktops .ws-btn.active {} /*Style for the active workspace button.*/
```

### Example
```css
.windows-desktops {
    padding: 0 4px 0 14px;
}
.windows-desktops {
    padding: 0 0px 0 10px;
}
.windows-desktops .widget-container {
    background-color: #11111b;
    margin: 4px 0 4px 0;
    border-radius: 12px;
}
.windows-desktops .ws-btn,
.windows-desktops .ws-btn-active {
    color: #7f849c;
    border: none;
    font-size: 14px;
    margin: 0 3px;
    padding: 0 
}
.windows-desktops .ws-btn-active {
    color: #89b4fa;
} 
```