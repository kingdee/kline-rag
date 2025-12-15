# #️⃣ Input Number 数值输入框

- 组件名: `kd-input-number`
- 说明: 数值输入框（Input Number）是用于数值输入的组件。

---

## 🛠️ API 属性

### Input.Number

以下表格描述了数值输入框组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `label` | 标题 | - | - | 1.0.0 |
| `name` | 数据提交标识 | - | - | 1.0.0 |
| `disabled` | 设置输入框**禁用状态** | `boolean` | `FALSE` | 1.0.0 |
| `read-only` | 设置输入框**只读状态** | `boolean` | `FALSE` | 1.0.0 |
| `required` | 设置是否**必录** | `boolean` | `FALSE` | 1.0.0 |
| `show-clear` | 是否展示**清除按钮** | `boolean` | `FALSE` | 1.0.0 |
| `value` | 输入框的值 | - | - | 1.0.0 |
| `placeholder` | 输入框为空时的提示语 | - | - | 1.0.0 |
| `auto-complete` | 自动填充，可选值包括 `off`、`on` | - | `off` | 1.0.0 |
| `size` | 输入框的尺寸，可选值包括 `large`、`medium`、`small` | - | `medium` | 1.0.0 |
| `state` | 反馈状态，可选值包括 `error`、`success` | - | - | 1.0.0 |
| `message` | 反馈提示语，设置 `state` 时显示 | - | - | 1.0.0 |
| `label-position` | 标题位置，可选值包括 `vertical`、`inline`、`hidden` | - | `vertical` | 1.0.0 |
| `variant` | 输入框的视觉样式变体，可选值包括 `underlined`、`outlined`、`borderless` | - | `outlined` | 1.0.0 |
| `min` | 允许输入的**最小值** | - | - | 1.0.0 |
| `max` | 允许输入的**最大值** | - | - | 1.0.0 |
| `precision` | **数值精度**（小数点位数），`0` 表示仅允许输入整数 | `number` | `0` | 1.0.0 |
| `formatter` | 数值显示的格式 | - | - | 1.0.0 |
| `show-stepper` | 是否显示**步进器** | `boolean` | `FALSE` | 1.0.0 |
| `stepper-style` | 步进器样式，可选值包括 `stepper`、`counter`；设置为 `counter` 时 `variant` 始终为 `outlined` | - | `stepper` | 1.0.0 |
| `step` | 步进器增减的**步长值** | `number` | `1` | 1.0.0 |
| `onfocus` | 获取焦点时触发 | - | - | 1.0.0 |
| `onblur` | 失去焦点时触发 | - | - | 1.0.0 |
| `onchange` | 值改变时触发 | - | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了数值输入框组件所使用的设计变量。这些变量与普通输入框（Input）通常是共享的。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-input-icon-color-default` | 图标默认颜色 | `var(--kdds-g-color-on-surface-3)` |
| `--kdds-c-input-icon-color-hover` | 图标悬停颜色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-input-icon-color-active` | 图标激活颜色 | `var(--kdds-g-color-accent-3)` |
| `--kdds-c-input-border-default` | 输入框默认边框颜色 | `var(--kdds-g-color-border-2)` |
| `--kdds-c-input-border-hover` | 输入框悬停边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-input-border-focus` | 输入框聚焦边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-input-border-error` | 输入框错误状态边框颜色 | `var(--kdds-g-color-border-error-3)` |
| `--kdds-c-input-border-disabled` | 输入框禁用状态边框颜色 | `var(--kdds-g-color-border-disabled-1)` |
| `--kdds-c-input-border-read-only` | 输入框只读状态边框颜色 | `var(--kdds-g-color-border-disabled-1)` |
| `--kdds-c-input-background-default` | 输入框默认背景颜色 | `var(--kdds-g-color-surface-container-1)` |
| `--kdds-c-input-background-disabled` | 输入框禁用状态背景颜色 | `var(--kdds-g-color-disabled-container-1)` |
| `--kdds-c-input-background-read-only` | 输入框只读状态背景颜色 | `var(--kdds-g-color-surface-container-1)` |
| `--kdds-c-input-value-color-default` | 输入框文本默认颜色 | `var(--kdds-g-color-on-surface-4)` |
| `--kdds-c-input-value-color-disabled` | 输入框禁用状态文本颜色 | `var(--kdds-g-color-disabled-1)` |
| `--kdds-c-input-value-color-read-only` | 输入框只读状态文本颜色 | `var(--kdds-g-color-on-surface-4)` |
| `--kdds-c-input-placeholder-color` | 输入框占位符文本颜色 | `var(--kdds-g-color-on-surface-1)` |
| `--kdds-c-input-field-label-color` | 字段标签颜色 | `var(--kdds-g-color-on-surface-4)` |
| `--kdds-c-input-required-indicator-color` | 必填指示器颜色 | `var(--kdds-g-color-on-error-1)` |
| `--kdds-c-input-supporting-text-color-success` | 辅助文本成功颜色 | `var(--kdds-g-color-success-1)` |
| `--kdds-c-input-supporting-text-color-error` | 辅助文本错误颜色 | `var(--kdds-g-color-error-1)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-input-value-font-size-small` | 输入框小尺寸文本字体大小 | `var(--kdds-g-font-scale-2)` |
| `--kdds-c-input-value-line-height-small` | 输入框小尺寸文本行高 | `var(--kdds-g-font-lineheight-4)` |
| `--kdds-c-input-value-font-size-medium` | 输入框中尺寸文本字体大小 | `var(--kdds-g-font-scale-3)` |
| `--kdds-c-input-value-line-height-medium` | 输入框中尺寸文本行高 | `var(--kdds-g-font-lineheight-5)` |
| `--kdds-c-input-value-font-size-large` | 输入框大尺寸文本字体大小 | `var(--kdds-g-font-scale-4)` |
| `--kdds-c-input-value-line-height-large` | 输入框大尺寸文本行高 | `var(--kdds-g-font-lineheight-4)` |
| `--kdds-c-input-icon-font-size` | 图标字体大小 | `var(--kdds-g-icon-sizing-3)` |
| `--kdds-c-input-field-label-font-size` | 字段标签字体大小 | `var(--kdds-g-font-scale-2)` |
| `--kdds-c-input-field-label-line-height` | 字段标签行高 | `var(--kdds-g-font-lineheight-4)` |
| `--kdds-c-input-required-indicator-font-size` | 必填指示器字体大小 | `var(--kdds-g-icon-sizing-1)` |
| `--kdds-c-input-supporting-text-font-size` | 辅助文本字体大小 | `var(--kdds-g-font-scale-2)` |
| `--kdds-c-input-supporting-text-line-height` | 辅助文本行高 | `var(--kdds-g-font-lineheight-4)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-input-shape-square-border-radius` | 输入框方形边框圆角 | `var(--kdds-g-radius-border-circle1)` |
| `--kdds-c-input-shape-round-border-radius` | 输入框圆形边框圆角 | `var(--kdds-g-radius-border-1)` |
| `--kdds-c-input-border-width` | 输入框边框宽度 | `var(--kdds-g-sizing-border-1)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-input-padding-horizontal-small` | 输入框小尺寸水平方向内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-input-padding-vertical-small` | 输入框小尺寸垂直方向内边距 | `var(--kdds-g-spacing-1)` |
| `--kdds-c-input-padding-horizontal-medium` | 输入框中尺寸水平方向内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-input-padding-vertical-medium` | 输入框中尺寸垂直方向内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-input-padding-horizontal-large` | 输入框大尺寸水平方向内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-input-padding-vertical-large` | 输入框大尺寸垂直方向内边距 | `calc(var(--kdds-g-spacing-3) + 1px)` |
| `--kdds-c-input-icon-margin-left` | 图标左间距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-input-field-label-margin-bottom` | 字段标签底间距 | `var(--kdds-g-spacing-2)` |
| `--kdds-c-input-supporting-text-margin-top` | 辅助文本上间距 | `var(--kdds-g-spacing-1)` |
| `--kdds-c-input-field-label-margin-right` | 字段标签右间距 | `var(--kdds-g-spacing-4)` |

### 动画 (Animation) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-input-icon-pointer-events` | 图标指针事件控制 | `auto` |
| `--kdds-c-input-icon-cursor` | 图标光标样式 | `pointer` |
| `--kdds-c-input-cursor-default` | 输入框默认光标样式 | `text` |
| `--kdds-c-input-cursor-disabled` | 输入框禁用状态光标样式 | `not-allowed` |
| `--kdds-c-input-cursor-read-only` | 输入框只读状态光标样式 | `default` |
| `--kdds-c-input-transition` | 输入框过渡动效 | `all 0.2s ease` |