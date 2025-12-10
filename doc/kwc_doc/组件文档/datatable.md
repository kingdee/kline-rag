# 📊 Datatable 表格

- 组件名: `kd-datatable`
- 说明: 表格（Datatable）用于展示结构化数据内容，通常还具备对数据进行操作的功能。

---

## 🛠️ API 属性

### Table (主组件)

以下表格描述了表格组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `columns` | 用于定义数据类型的列对象数组。**必须包含** `'label'`、`'fieldName'` 和 `'type'` | `array` | - | 1.0.0 |
| `data` | 要显示的数组数据 | `array` | - | 1.0.0 |
| `hide-checkbox-column` | 隐藏行选择的复选框或单选框列 | `boolean` | `false` | 1.0.0 |
| `key-field` | 用于关联每行唯一标识的字段，区分大小写，**必须**与数据数组中的值匹配 | `string` | - | 1.0.0 |
| `max-row-selection` | 最大可选行数，值为正整数。默认为复选框选择，值为 `1` 时为单选 | `number` | - | 1.0.0 |
| `selected-rows` | 通过 `key-field` 值列表实现程序化行选择 | `array` | - | 1.0.0 |
| `show-row-number-column` | 设置是否在第一列显示行号 | `boolean` | `false` | 1.0.0 |
| `single-row-selection-mode` | 当 `max-row-selection` 为 `1` 时，是否强制使用复选框而非单选按钮 | `boolean` | `false` | 1.0.0 |

### Columns (列定义)

以下表格描述了表格列定义对象 (`Columns`) 的属性。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `label` | **必填**。列字段标题 | `string` | - | 1.0.0 |
| `fieldName` | **必填**。将列属性绑定到相关数据的名称。每个列属性必须与数据数组中的某个项目相对应 | `string` | - | 1.0.0 |
| `type` | **必填**。数据类型 | `string` | `'text'` | 1.0.0 |
| `cellAttributes` | 使用 `alignment` 设置列对齐方式（`right`，`center`，`left`）， `class` 属性提供额外的自定义，除了 `icon*` 属性（例如用于向单元格添加图标）。有关更多信息，请参阅向列数据中添加图标 | `object` | - | 1.0.0 |
| `fixedWidth` | 指定列的像素宽度并使列不可调整大小。如果同时提供了 `fixedWidth` 和 `initialWidth` 的值，则忽略 `initialWidth` | `number` | - | 1.0.0 |
| `hideLabel` | 指定是否隐藏列上的标签 | `boolean` | `FALSE` | 1.0.0 |
| `initialWidth` | 初始化时列的宽度，必须在 `min-column-width` 和 `max-column-width` 值之间，或者在没有提供的情况下，在 `50px` 和 `1000px` 之间 | `number` | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了表格组件所使用的设计变量。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-datatable-background` | 表格整体背景色 | `var(--kdds-g-color-surface-container-1)` |
| `--kdds-c-datatable-header-background` | 表头背景色 | `var(--kdds-g-color-surface-container-3)` |
| `--kdds-c-datatable-cell-background` | 单元格背景色 | `var(--kdds-g-color-surface-container-1)` |
| `--kdds-c-datatable-row-background-hover` | 行悬停状态背景色 | `var(--kdds-g-color-surface-container-2)` |
| `--kdds-c-datatable-row-background-active` | 行选中状态背景色 | `var(--kdds-g-color-accent-5)` |
| `--kdds-c-datatable-cell-edit-background-hover` | 可编辑单元格背景色 | `var(--kdds-g-color-surface-container-1)` |
| `--kdds-c-datatable-expand-row-background` | 表格行展开背景色 | `var(--kdds-g-color-neutral-base-92)` |
| `--kdds-c-datatable-cell-border` | 单元格边框颜色 | `var(--kdds-g-color-border-2)` |
| `--kdds-c-datatable-cell-border-focus` | 单元格聚焦边框色 | `var(--kdds-g-color-accent-1)` |
| `--kdds-c-datatable-cell-edit-border` | 可编辑单元格默认边框色 | `var(--kdds-g-color-border-2)` |
| `--kdds-c-datatable-cell-edit-border-hover` | 可编辑单元格悬停后边框色 | `var(--kdds-g-color-border-accent-1)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-datatable-grid-padding-left` | 单元格内容左边距 | `var(--kdds-g-spacing-2)` |
| `--kdds-c-datatable-grid-padding-right` | 单元格内容右边距 | `var(--kdds-g-spacing-2)` |
| `--kdds-c-datatable-column-header-padding-left` | 表头内容左边距 | `var(--kdds-g-spacing-5)` |
| `--kdds-c-datatable-column-header-padding-right` | 表头内容右边距 | `var(--kdds-g-spacing-5)` |
| `--kdds-c-datatable-cell-padding` | 单元格边距 | `var(--kdds-g-spacing-2)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-datatable-cell-border-width` | 单元格边框大小 | `var(--kdds-g-sizing-border-1)` |
| `--kdds-c-datatable-cell-edit-border-radius` | 可编辑单元格边框圆角 | `var(--kdds-g-radius-border-1)` |
| `--kdds-c-datatable-cell-edit-border-width` | 可编辑单元格边框宽度 | `var(--kdds-g-sizing-border-1)` |

### 尺寸 (Sizing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-datatable-header-line-height` | 表头高度 | `1.75rem` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-datatable-cell-color` | 单元格文字颜色 | `var(--kdds-g-color-on-surface-4)` |

### 阴影 (Shadow) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `shadow--kdds-c-datatable-fixed-shadow` | 固定列投影 | `color gradient (#000,100%～#000,15%)` |