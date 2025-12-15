# 💬 Toast 消息提示

- 组件名: `kd-toast`
- 说明: 消息提示（Toast）是用户操作后的一种反馈和确认机制。

---

## 🛠️ API 属性

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `message` | 消息内容 | `string` | - | 1.0.0 |
| `messageLinks` | 设置内容超链接 | `array` | - | 1.0.0 |
| `duration` | 自动关闭的延时，单位为秒，设为 `0` 时不自动关闭 | `number` | `3` | 1.0.0 |
| `variant` | 消息的视觉样式变体，可选值包括 `error`、`warning`、`success` | `string` | `success` | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了消息提示组件所使用的设计变量。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-toast-color-success` | 成功状态文字颜色 | `var(--kdds-g-color-success-1,#1BA854)` |
| `--kdds-c-toast-background-success` | 成功状态背景色 | `var(--kdds-g-color-success-container-1,#DCFAE4)` |
| `--kdds-c-toast-border-success` | 成功状态边框色 | `var(--kdds-g-color-border-success-1,#A1E6B5)` |
| `--kdds-c-toast-color-warning` | 警告状态文字颜色 | `var(--kdds-g-color-warning-1,#FF991C)` |
| `--kdds-c-toast-background-warning` | 警告状态背景色 | `var(--kdds-g-color-warning-container-1,#FFF1D4)` |
| `--kdds-c-toast-border-warning` | 警告状态边框色 | `var(--kdds-g-color-border-warning-1,#FFE0A6)` |
| `--kdds-c-toast-color-error` | 失败状态文字颜色 | `var(--kdds-g-color-error-1,#FB2323)` |
| `--kdds-c-toast-background-error` | 失败状态背景色 | `var(--kdds-g-color-error-container-1,#FFDBE0)` |
| `--kdds-c-toast-border-error` | 失败状态边框色 | `var(--kdds-g-color-border-error-1,#FFADB6)` |
| `--kdds-c-toast-link` | 文本链接颜色 | `var(--kdds-g-color-on-surface-link-1,#0E5FD8)` |
| `--kdds-c-toast-link-hover` | 文本链接悬停色 | `var(--kdds-g-color-on-surface-link-2,#3987ED)` |
| `--kdds-c-toast-link-active` | 文本链接激活色 | `var(--kdds-g-color-on-surface-link-3,#0041B0)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-toast-line-height` | 文字行高 | `var(--kdds-g-font-lineheight-5,1.572)` |
| `--kdds-c-toast-font-size` | 文字大小 | `var(--kdds-g-font-scale-3,0.875rem)` |
| `--kdds-c-toast-icon-font-size` | 图标字体大小 | `var(--kdds-g-icon-sizing-3,1rem)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-toast-border-radius` | 边框圆角 | `var(--kdds-g-spacing-2,0.25rem)` |
| `--kdds-c-toast-border-width` | 边框宽度 | `var(--kdds-g-sizing-border-1,1px)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-toast-prefixicon-margin-right` | 前缀图标右外边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `--kdds-c-toast-padding-vertical` | 上下内边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `--kdds-c-toast-padding-horizontal` | 左右内边距 | `calc(var(--kdds-g-spacing-5)-1px,0.75rem-1px)` |
| `--kdds-c-toast-gap` | 组件之间的间距 | `var(--kdds-g-spacing-6,1rem)` |
| `--kdds-c-toast-viewport-gap` | 组件与窗口的最小宽度 | `var(--kdds-g-spacing-4,0.5rem)` |
| `--kdds-c-toast-close-margin-left` | 关闭按钮左外边距 | `var(--kdds-g-spacing-5,0.75rem)` |

### 尺寸 (Sizing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-toast-sizing-min-width` | 最小宽度 | `17.5rem` |
| `--kdds-c-toast-sizing-max-width` | 最大宽度 | `62.5rem` |
| `--kdds-c-toast-sizing-max-height` | 最大高度 | `10rem` |