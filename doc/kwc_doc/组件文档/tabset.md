# 📑 Tabset 选项卡

- 组件名: `kd-tabset`
- 说明: 选项卡（Tabset）是选项卡切换组件。

---

## 🛠️ API 属性

### tabset (容器组件)

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `active-tab-value` | 默认激活的选项卡，若不配置则默认激活第一个选项卡 | - | - | 1.0.0 |
| `size` | 选项卡的尺寸，可选值包括 `large`、`medium`、`small` | - | `medium` | 1.0.0 |
| `ontabchange` | 激活的选项卡发生变化时触发 | - | - | 1.0.0 |

### tab (子项组件)

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `icon-name` | 选项卡图标 | - | - | 1.0.0 |
| `label` | 选项卡标题 | - | - | 1.0.0 |
| `show-error-indicator` | 指定选项卡内容中是否有错误，错误图标显示在选项卡标签的右侧 | `boolean` | `FALSE` | 1.0.0 |
| `value` | 用于在选项卡的 active 事件期间标识已单击哪个选项卡的可选字符串；此字符串还被 `tabset` 中的 `active-tab-value` 用来打开选项卡 | - | - | 1.0.0 |
| `onloadcontent` | 内容加载时触发 | - | 暂不支持 |

---

## 🧩 插槽 (Slots)

### tabset 插槽

| 名称 | 说明 | 版本 |
| :--- | :--- | :--- |
| `default` | `tabset` 默认插槽。通过这个插槽，可以将多个 `tab` 组件插入到 `tabset` 中 | 1.0.0 |

### tab 插槽

| 名称 | 说明 | 版本 |
| :--- | :--- | :--- |
| `default` | `tab` 组件中的内容占位区域 | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了选项卡组件所使用的设计变量。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-tabset-underlined-border` | 普通状态边框颜色 | `var(--kdds-g-color-border-1,#E5E5E5)` |
| `--kdds-c-tabset-underlined-border-active` | 选中态边框颜色 | `var(--kdds-g-color-border-accent-1,#5582F3)` |
| `--kdds-c-tabset-underlined-background` | 默认背景 | `var(--kdds-g-color-surface-1,#FFFFFF)` |
| `--kdds-c-tabset-color` | 文字默认颜色 | `var(--kdds-g-color-on-surface-3,#666666)` |
| `--kdds-c-tabset-color-active` | 文字选中颜色 | `var(--kdds-g-color-accent-1,#5582F3)` |
| `--kdds-c-tabset-color-hover` | 文字悬停颜色 | `var(--kdds-g-color-accent-1,#5582F3)` |
| `--kdds-c-tabset-color-disabled` | 文字禁用颜色 | `var(--kdds-g-color-on-surface-1,#B2B2B2)` |
| `--kdds-c-tabset-dropdown-color` | 下拉图标默认颜色 | `var(--kdds-g-color-on-surface-1,#B2B2B2)` |
| `--kdds-c-tabset-dropdown--color-hover` | 下拉图标悬停颜色 | `var(--kdds-g-color-on-surface-3,#666666)` |
| `--kdds-c-tabset-dropdown-color-active` | 下拉图标激活颜色 | `var(--kdds-g-color-on-surface-3,#666666)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-tabset-font-size-small` | 线性页签小尺寸字号 | `var(--kdds-g-font-scale-2,0.75rem)` |
| `--kdds-c-tabset-line-height-small` | 线性页签小尺寸行高 | `var(--kdds-g-font-lineheight-4,1.5)` |
| `--kdds-c-tabset-prefixicon-font-size-small` | 线性页签小尺寸前缀图标大小 | `var(--kdds-g-icon-sizing-2,0.75rem)` |
| `--kdds-c-tabset-dropdown-font-size-small` | 线性页签小尺寸下拉图标大小 | `var(--kdds-g-icon-sizing-2,0.75rem)` |
| `--kdds-c-tabset-font-size-medium` | 线性页签中尺寸字号 | `var(--kdds-g-font-scale-3,0.875rem)` |
| `--kdds-c-tabset-line-height-medium` | 线性页签中尺寸行高 | `var(--kdds-g-font-lineheight-5,1.572)` |
| `--kdds-c-tabset-prefixicon-font-size-medium` | 线性页签中尺寸前缀图标大小 | `var(--kdds-g-icon-sizing-3,1rem)` |
| `--kdds-c-tabset-dropdown-font-size-medium` | 线性页签中尺寸下拉图标大小 | `var(--kdds-g-icon-sizing-3,1rem)` |
| `--kdds-c-tabset-font-size-large` | 线性页签大尺寸字号 | `var(--kdds-g-font-scale-4,1rem)` |
| `--kdds-c-tabset-line-height-large` | 线性页签大尺寸行高 | `var(--kdds-g-font-lineheight-4,1.5)` |
| `--kdds-c-tabset-prefixicon-font-size-large` | 线性页签大尺寸前缀图标大小 | `var(--kdds-g-icon-sizing-4,1.25rem)` |
| `--kdds-c-tabset-dropdown-font-size-large` | 线性页签大尺寸下拉图标大小 | `var(--kdds-g-icon-sizing-4,1.25rem)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-tabset-underlined-border-style` | 边框样式 | `solid` |
| `--kdds-c-tabset-underlined-border-width-bottom` | 普通状态底部边框宽度 | `var(--kdds-g-sizing-border-1,1px)` |
| `--kdds-c-tabset-underlined-border-width-bottom-active` | 激活状态底部边框宽度 | `var(--kdds-g-sizing-border-2,2px)` |

### 尺寸 (Sizing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-tabset-underlined-tab-sizing-min-width` | 线性页签最小宽度 | `52px` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-tabset-underlined-tab-padding-horizontal` | 线性页签水平内边距 | `20px` |
| `--kdds-c-tabset-prefixicon-margin-right` | 前缀图标右侧间距 | `var(--kdds-g-spacing-2,0.25rem)` |
| `--kdds-c-tabset-suffixicon-margin-left` | 报错图标左侧间距 | `var(--kdds-g-spacing-2,0.25rem)` |
| `--kdds-c-tabset-underlined-padding-top-small` | 线性页签小尺寸上间距 | `var(--kdds-g-spacing-3,0.375rem)` |
| `--kdds-c-tabset-underlined-padding-bottom-small` | 线性页签小尺寸下间距 | `calc(var(--kdds-g-spacing-3)+1px,0.375rem+1px)` |
| `--kdds-c-tabset-underlined-padding-top-medium` | 线性页签中尺寸上间距 | `calc(var(--kdds-g-spacing-4)+2px,0.5rem+2px)` |
| `--kdds-c-tabset-underlined-padding-bottom-medium` | 线性页签中尺寸下间距 | `calc(var(--kdds-g-spacing-4)+3px,0.5rem+3px)` |
| `--kdds-c-tabset-underlined-padding-top-large` | 线性页签大尺寸上间距 | `var(--kdds-g-spacing-5,0.75rem)` |
| `--kdds-c-tabset-underlined-padding-bottom-large` | 线性页签大尺寸下间距 | `calc(var(--kdds-g-spacing-5)+1px,0.75rem+1px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-horizontal-small` | 线性页签小尺寸下拉容器水平间距 | `calc(var(--kdds-g-spacing-4)+2px,0.5rem+2px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-top-small` | 线性页签小尺寸下拉容器上间距 | `calc(var(--kdds-g-spacing-4)+2px,0.5rem+2px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-bottom-small` | 线性页签小尺寸下拉容器下间距 | `calc(var(--kdds-g-spacing-4)+1px,0.5rem+1px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-horizontal-medium` | 线性页签中尺寸下拉容器水平间距 | `calc(var(--kdds-g-spacing-5)+2px,0.75rem+2px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-top-medium` | 线性页签中尺寸下拉容器上间距 | `calc(var(--kdds-g-spacing-5)+2px,0.75rem+2px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-bottom-medium` | 线性页签中尺寸下拉容器下间距 | `calc(var(--kdds-g-spacing-5)+1px,0.75rem+1px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-horizontal-large` | 线性页签大尺寸下拉容器水平间距 | `calc(var(--kdds-g-spacing-6)-1px,1rem-1px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-top-large` | 线性页签大尺寸下拉容器上间距 | `calc(var(--kdds-g-spacing-6)-1px,1rem-1px)` |
| `--kdds-c-tabset-underlined-dropdown-padding-bottom-large` | 线性页签大尺寸下拉容器下间距 | `calc(var(--kdds-g-spacing-5)+2px,0.75rem+2px)` |