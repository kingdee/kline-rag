# 📌 Checkbox 复选框

- 组件名: `kd-checkbox`
- 说明: 复选框（Checkbox）是可构成复选框组，供用户选择的单个选项。

---

## API 属性

以下表格描述了复选框组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `label` | 选项标题 | `string` | - | 1.0.0 |
| `checked` | 用于指定当前单选框是否选中，是一个**受控属性**（在 group 中使用时无效） | `boolean` | `FALSE` | 1.0.0 |
| `default-checked` | 用于设置单选框的**初始选中状态**，是一个**非受控属性**。只在首次渲染时起作用（在 group 中使用时无效） | `boolean` | `FALSE` | 1.0.0 |
| `indeterminate` | 设置**半选状态**，只负责样式控制 | `boolean` | `FALSE` | 1.0.0 |
| `disabled` | 设置复选框**禁用状态** | `boolean` | `FALSE` | 1.0.0 |
| `read-only` | 设置复选框**只读状态** | `boolean` | `FALSE` | 1.0.0 |
| `value` | 选项值 | - | - | 1.0.0 |
| `onchange` | 选中状态改变时触发的事件 | - | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了复选框组件所使用的设计变量，按类别分为颜色、尺寸、边框和排版。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-unselected-color` | 未选图标色 | `var(--kdds-g-color-on-surface-3,#666666)` |
| `--kdds-c-checkbox-unselected-background` | 未选图标背景色 | `var(--kdds-g-color-surface-container-1,#FFFFFF)` |
| `--kdds-c-checkbox-unselected-color-hover` | 未选图标悬停色 | `var(--kdds-g-color-accent-1,#5582F3)` |
| `--kdds-c-checkbox-unselected-color-active` | 未选图标选中色 | `var(--kdds-g-color-accent-1,#5582F3)` |
| `--kdds-c-checkbox-unselected-color-disabled` | 未选图标禁用色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-unselected-color-read-only` | 未选图标只读色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-unselected-border-read-only` | 未选边框只读色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-selected-color` | 选中图标色 | `var(--kdds-g-color-accent-1,#5582F3)` |
| `--kdds-c-checkbox-selected-color-disabled` | 选中图标禁用色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-selected-background-disabled` | 选中图标禁用背景色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-selected-border-color-disabled` | 选中图标禁用边框色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-selected-color-read-only` | 选中图标只读色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-selected-background-read-only` | 选中图标只读背景色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-selected-border-color-read-only` | 选中图标只读边框色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-intermediate-color` | 半选图标色 | `var(--kdds-g-color-accent-1,#5582F3)` |
| `--kdds-c-checkbox-intermediate-color-disabled` | 半选图标禁用色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-intermediate-background-disabled` | 半选图标禁用背景色 | `var(--kdds-g-color-disabled-container-1,#F5F5F5)` |
| `--kdds-c-checkbox-intermediate-border-color-disabled` | 半选图标禁用边框色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-intermediate-background-disabled` | 半选图标禁用背景色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-intermediate-color-read-only` | 半选图标只读色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-intermediate-background-read-only` | 半选图标只读背景色 | `var(--kdds-g-color-disabled-container-1,#F5F5F5)` |
| `--kdds-c-checkbox-intermediate-border-color-read-only` | 半选图标只读边框色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-color` | 文字默认色 | `var(--kdds-g-color-on-surface-4,#212121)` |
| `--kdds-c-checkbox-color-hover` | 文字悬停色 | `var(--kdds-g-color-on-surface-4,#212121)` |
| `--kdds-c-checkbox-color-active` | 文字选中色 | `var(--kdds-g-color-on-surface-4,#212121)` |
| `--kdds-c-checkbox-color-disabled` | 文字禁用色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-checkbox-color-read-only` | 文字只读色 | `var(--kdds-g-color-on-surface-4,#212121)` |

### 尺寸 (Sizing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-unselected-sizing` | 外圆尺寸 | `var(--kdds-g-icon-sizing-3,1rem)` |
| `--kdds-c-checkbox-selected-sizing` | 内圆尺寸 | `var(--kdds-g-icon-sizing-2,0.75rem)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-border-radius` | 圆角值 | `var(--kdds-g-radius-border-1,0.125rem)` |
| `--kdds-c-checkbox-border-width` | 宽边宽度 | `var(--kdds-g-sizing-border-1,0.0625rem)` |
| `--kdds-c-checkbox-border` | 宽边宽度全透明 | `transprant` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-icon-padding-right` | 图标右内边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `--kdds-c-checkbox-item-padding-right` | 选项右内边距 | `var(--kdds-g-spacing-6,1rem)` |
| `--kdds-c-checkbox-padding-vertical` | 上下内边距 | `var(--kdds-g-spacing-2,0.25rem)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-label-font-size` | 字体尺寸 | `var(--kdds-g-font-scale-3，0.875rem)` |
| `--kdds-c-checkbox-label-font-line-height` | 字体行高 | `var(--kdds-g-font-lineheight-5,1.571)` |