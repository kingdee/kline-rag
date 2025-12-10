# 👆 Button 按钮

- 组件名: `kd-button`
- 说明: 按钮（Button）是一种用于触发特定操作的组件。

---

## 🛠️ API 属性

以下表格描述了按钮组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `label` | 按钮内显示的文本内容。 | - | - | 1.0.0 |
| `icon-name` | 按钮图标 | - | - | 1.0.0 |
| `icon-position` | 图标位置，可选值包括 `left`、`right` | - | `left` | 1.0.0 |
| `disabled` | 设置按钮**禁用状态** | `boolean` | `FALSE` | 1.0.0 |
| `loading` | 设置按钮**加载状态** | `boolean` | `FALSE` | 1.0.0 |
| `stretch` | 开启该属性按钮将**撑满父元素** | `boolean` | `FALSE` | 1.0.0 |
| `shape` | 按钮的形状，可选值包括 `square`、`round`、`circle` | - | `square` | 1.0.0 |
| `size` | 按钮的尺寸，可选值包括 `large`、`medium`、`small` | - | `medium` | 1.0.0 |
| `variant` | 按钮的视觉样式变体，可选值包括 `primary` (主要)、`ghost` (幽灵/线框)、`secondary` (次要) 和 `text` (文字) | - | `primary` | 1.0.0 |
| `onclick` | 点击时触发的事件 | - | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了按钮组件所使用的设计变量，按类别分为颜色、排版、间距、尺寸、边框和透明度。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-button-primary-background` | 主要按钮背景颜色 | `var(--kdds-g-color-accent-container-1)` |
| `--kdds-c-button-primary-color` | 主要按钮文字颜色 | `var(--kdds-g-color-accent-5)` |
| `--kdds-c-button-primary-border` | 主要按钮边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-button-primary-background-hover` | 主要按钮悬停时的背景颜色 | `var(--kdds-g-color-accent-container-2)` |
| `--kdds-c-button-primary-border-hover` | 主要按钮悬停时的边框颜色 | `var(--kdds-g-color-border-accent-2)` |
| `--kdds-c-button-primary-background-active` | 主要按钮激活时的背景颜色 | `var(--kdds-g-color-accent-container-3)` |
| `--kdds-c-button-primary-border-active` | 主要按钮激活时的边框颜色 | `var(--kdds-g-color-border-accent-3)` |
| `--kdds-c-button-primary-background-disabled` | 主要按钮禁用时的背景颜色 | `var(--kdds-g-color-accent-container-4)` |
| `--kdds-c-button-primary-border-disabled` | 主要按钮禁用时的边框颜色 | `var(--kdds-g-color-border-accent-4)` |
| `--kdds-c-button-primary-color-disabled` | 主要按钮禁用时文字颜色的 | `var(--kdds-g-color-accent-4)` |
| `--kdds-c-button-primary-background-loading` | 主要按钮加载时的背景颜色 | `var(--kdds-g-color-accent-container-1)` |
| `--kdds-c-button-primary-border-loading` | 主要按钮加载时的边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-button-primary-color-loading` | 主要按钮加载时的文字颜色 | `var(--kdds-g-color-accent-4)` |
| `--kdds-c-button-primary-loading-icon-color` | 主要按钮加载图标颜色 | `var(--kdds-g-color-on-surface-inverse-1)` |
| `--kdds-c-button-ghost-border` | 幽灵按钮边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-button-ghost-color` | 幽灵按钮文字颜色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-button-ghost-border-hover` | 幽灵按钮悬停时的边框颜色 | `var(--kdds-g-color-border-accent-2)` |
| `--kdds-c-button-ghost-color-hover` | 幽灵按钮悬停时的文字颜色 | `var(--kdds-g-color-accent-2)` |
| `--kdds-c-button-ghost-border-active` | 幽灵按钮激活时的边框颜色 | `var(--kdds-g-color-border-accent-3)` |
| `--kdds-c-button-ghost-color-active` | 幽灵按钮激活时的文字颜色 | `var(--kdds-g-color-accent-3)` |
| `--kdds-c-button-ghost-border-disabled` | 幽灵按钮禁用时的边框颜色 | `var(--kdds-g-color-border-2)` |
| `--kdds-c-button-ghost-color-disabled` | 幽灵按钮禁用时的文字颜色 | `var(--kdds-g-color-on-surface-1)` |
| `--kdds-c-button-ghost-border-loading` | 幽灵按钮加载时的边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-button-ghost-color-loading` | 幽灵按钮加载时的文字颜色 | `var(--kdds-g-color-accent-4)` |
| `--kdds-c-button-ghost-loading-icon-color` | 幽灵按钮加载图标颜色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-button-secondary-background` | 次要按钮背景颜色 | `var(--kdds-g-color-surface-container-1)` |
| `--kdds-c-button-secondary-border` | 次要按钮边框颜色 | `var(--kdds-g-color-border-2)` |
| `--kdds-c-button-secondary-color` | 次要按钮文字颜色 | `var(--kdds-g-color-on-surface-4)` |
| `--kdds-c-button-secondary-border-hover` | 次要按钮悬停时的边框颜色 | `var(--kdds-g-color-border-accent-1)` |
| `--kdds-c-button-secondary-color-hover` | 次要按钮悬停时的文字颜色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-button-secondary-border-active` | 次要按钮激活时的边框颜色 | `var(--kdds-g-color-border-accent-3)` |
| `--kdds-c-button-secondary-color-active` | 次要按钮激活时的文字颜色 | `var(--kdds-g-color-accent-3)` |
| `--kdds-c-button-secondary-background-disabled` | 次要按钮禁用时的背景颜色 | `var(--kdds-g-color-disabled-container-1)` |
| `--kdds-c-button-secondary-border-disabled` | 次要按钮禁用时的边框颜色 | `var(--kdds-g-color-border-disabled-1)` |
| `--kdds-c-button-secondary-color-disabled` | 次要按钮禁用时的文字颜色 | `var(--kdds-g-color-disabled-1)` |
| `--kdds-c-button-secondary-border-loading` | 次要按钮加载时的边框颜色 | `var(--kdds-g-color-border-2)` |
| `--kdds-c-button-secondary-color-loading` | 次要按钮加载时的文字颜色 | `var(--kdds-g-color-on-surface-1)` |
| `--kdds-c-button-secondary-loading-icon-color` | 次要按钮加载图标颜色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-button-text-color-hover` | 文字按钮悬停时的颜色 | `var(--kdds-g-color-accent-2)` |
| `--kdds-c-button-text-color-active` | 文字按钮激活时的颜色 | `var(--kdds-g-color-accent-3)` |
| `--kdds-c-button-text-color-disabled` | 文字按钮禁用时的颜色 | `var(--kdds-g-color-disabled-1)` |
| `--kdds-c-button-text-color-loading` | 文字按钮加载时的颜色 | `var(--kdds-g-color-accent-4)` |
| `--kdds-c-button-text-loading-icon-color` | 文字按钮加载图标颜色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-button-text-color` | 文字按钮的颜色 | `var(--kdds-g-color-accent-1)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-button-font-size-small` | 小号按钮字体大小 | `var(--kdds-g-font-scale-2)` |
| `--kdds-c-button-line-height-small` | 小号按钮行高 | `var(--kdds-g-font-lineheight-4)` |
| `--kdds-c-button-font-size-medium` | 中号按钮字体大小 | `var(--kdds-g-font-scale-3)` |
| `--kdds-c-button-line-height-medium` | 中号按钮行高 | `var(--kdds-g-font-lineheight-5)` |
| `--kdds-c-button-font-size-large` | 大号按钮字体大小 | `var(--kdds-g-font-scale-4)` |
| `--kdds-c-button-line-height-large` | 大号按钮行高 | `var(--kdds-g-font-lineheight-4)` |
| `--kdds-c-button-icon-font-size` | 按钮里的图标尺寸大小 | `var(--kdds-g-icon-sizing-3)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-button-padding-vertical-small` | 小号按钮上下内边距 | `var(--kdds-g-spacing-1)` |
| `--kdds-c-button-padding-horizontal-small` | 小号按钮左右内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-button-padding-vertical-medium` | 中号按钮上下内边距 | `var(--kdds-g-spacing-2)` |
| `--kdds-c-button-padding-horizontal-medium` | 中号按钮左右内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-button-padding-vertical-large` | 大号按钮上下内边距 | `calc(var(--kdds-g-spacing-3) + 1px)` |
| `--kdds-c-button-padding-horizontal-large` | 大号按钮左右内边距 | `var(--kdds-g-spacing-5)` |
| `--kdds-c-button-prefixicon-margin-right` | 前缀图标右外边距 | `var(--kdds-g-spacing-2)` |
| `--kdds-c-button-suffixicon-margin-left` | 后缀图标左外边距 | `var(--kdds-g-spacing-2)` |

### 尺寸 (Sizing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-button-sizing-min-width-small` | 小号按钮最小宽度 | `3.75rem` |
| `--kdds-c-button-sizing-max-width-small` | 小号按钮最大宽度 | `100%` |
| `--kdds-c-button-sizing-min-width-medium` | 中号按钮最小宽度 | `3.75rem` |
| `--kdds-c-button-sizing-max-width-medium` | 中号按钮最大宽度 | `100%` |
| `--kdds-c-button-sizing-min-width-large` | 大号按钮最小宽度 | `4.25rem` |
| `--kdds-c-button-sizing-max-width-large` | 大号按钮最大宽度 | `100%` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-button-shape-square-border-radius` | 圆角方形按钮 | `var(--kdds-g-radius-border-1)` |
| `--kdds-c-button-shape-round-border-radius` | 全圆角按钮 | `var(--kdds-g-radius-border-circle1)` |
| `--kdds-c-button-border-width` | 按钮边框宽度 | `var(--kdds-g-sizing-border-1)` |

### 透明度 (Opacity) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-button-ghost-background` | 幽灵按钮背景透明度 | `var(--kdds-g-opacity-0)` |
| `--kdds-c-button-custom-opacity-hover` | 自定义按钮悬停透明度 | `var(--kdds-g-opacity-60)` |
| `--kdds-c-button-custom-opacity-disabled` | 自定义按钮禁用透明度 | `var(--kdds-g-opacity-20)` |
| `--kdds-c-button-custom-loading-icon-color` | 自定义按钮加载图标透明度 | `var(--kdds-g-opacity-40)` |

## 事件事例代码：
```html
<kd-button variant="primary" onclick={handleSave}>保存</kd-button>
```