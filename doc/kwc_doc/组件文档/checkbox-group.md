# 📦 Checkbox Group 复选框组

- 组件名: `kd-checkbox-group`
- 说明: 复选框组 (`checkbox-group`) 用于实现单选或多选功能的复选框集合。

---

## API 属性

以下表格描述了复选框组组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `label` | 多选组的标题 | - | - | 1.0.0 |
| `disabled` | 设置**整组选项禁用状态**，`checkbox-group` 优先级高于 `checkbox` | `boolean` | `FALSE` | 1.0.0 |
| `read-only` | 设置**整组选项只读状态**，`checkbox-group` 优先级高于 `checkbox` | `boolean` | `FALSE` | 1.0.0 |
| `required` | 设置是否**必录** | `boolean` | `FALSE` | 1.0.0 |
| `label-position` | 标题位置，可选值包括 `vertical`、`inline`、`hidden` | - | `vertical` | 1.0.0 |
| `state` | 反馈状态，可选值包括 `error` | - | - | 1.0.0 |
| `message` | 反馈提示语，设置 `state` 时显示 | - | - | 1.0.0 |
| `value` | 当前选中的选项值 | - | - | 1.0.0 |
| `default-value` | 默认选中的选项值 | - | - | 1.0.0 |
| `name` | 数据提交标识 | `string` | - | 1.0.0 |
| `options` | 指定可选项配置数组 | `array` | - | 1.0.0 |
| `layout` | 选项布局方式，可选值包括 `vertical`、`horizontal` | - | `horizontal` | 1.0.0 |
| `onchange` | 当 `checkbox-group` 中任何一个复选框的选中状态发生改变时触发 | - | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了复选框组组件所使用的设计变量，按类别分为颜色、间距和排版。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-group-field-label-color` | 默认字体色 | `var(--kdds-g-color-on-surface-4,#212121)` |
| `--kdds-c-checkbox-group-required-indicator-color` | 必录图标颜色 | `var(--kdds-g-color-on-error-1,#FB2323)` |
| `--kdds-c-checkbox-group-supporting-text-color-error` | 字体错误色 | `var(--kdds-g-color-on-error-1,#FB2323)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-group-field-label-margin-bottom` | 标题下外边距 | `var(--kdds-g-spacing-2, 0.25rem)` |
| `--kdds-c-checkbox-group-field-label-margin-top` | 标题上外边距 | `var(--kdds-g-spacing-1,0.125rem)` |
| `--kdds-c-checkbox-group-field-label-margin-right` | 水平标题下的右间距 | `var(--kdds-g-spacing-4,0.5rem)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-checkbox-group-field-label-font-size` | 字体大小 | `var(--kdds-g-font-scale-2,0.875rem)` |
| `--kdds-c-checkbox-group-field-label-line-height` | 字体行高 | `var(--kdds-g-font-lineheight-4,1.5)` |
| `--kdds-c-checkbox-group-required-indicator-font-size` | 必录图标大小 | `var(--kdds-g-icon-sizing-1,0.5rem)` |
| `--kdds-c-checkbox-group-supporting-text-font-size-error` | 字体大小（错误提示） | `var(--kdds-g-font-scale-2,0.875rem)` |
| `--kdds-c-checkbox-group-supporting-text-font-line-height-error` | 字体行高（错误提示） | `var(--kdds-g-font-lineheight-4,1.5)` |