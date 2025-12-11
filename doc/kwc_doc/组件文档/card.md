# 📄 Card 卡片

- 组件名: `kd-card`
- 说明: 卡片（Card）是一种通用的卡片容器组件。

---

## 🛠️ API 属性

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `hide-header` | 隐藏头部栏 | `boolean` | `false` | 1.0.0 |
| `icon-name` | 标题前的图标 | `string` | - | 1.0.0 |
| `title` | 标题 | `string` | - | 1.0.0 |

---

## 🧩 插槽 (Slots)

| 名称 | 说明 | 版本 |
| :--- | :--- | :--- |
| `title` | 自定义渲染标题区域 | 1.0.0 |
| `actions` | 自定义渲染操作区域 | 1.0.0 |
| `footer` | 自定义渲染底部区域 | 1.0.0 |
| `default` | 自定义渲染内容区域（主体） | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了卡片组件所使用的设计变量。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-card-background` | 卡片背景色 | `var(--kdds-g-color-surface-1)` |
| `--kdds-c-card-border` | 卡片边框色 | `var(--kdds-g-color-border-1)` |
| `--kdds-c-card-header-background` | 卡片头部区域背景色 | `var(--kdds-g-color-surface-1)` |
| `--kdds-c-card-icon-color` | 卡片图标颜色 | `var(--kdds-g-color-on-surface-3)` |
| `--kdds-c-card-title-color` | 卡片标题文字颜色 | `var(--kdds-g-color-on-surface-4)` |
| `--kdds-c-card-text-color` | 卡片正文文字颜色 | `var(--kdds-g-color-on-surface-4)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-card-title-font-size` | 卡片标题文字大小 | `var(--kdds-g-font-scale-4)` |
| `--kdds-c-card-title-font-weight` | 卡片标题字重 | `var(--kdds-g-font-weight-6)` |
| `--kdds-c-card-title-line-height` | 卡片标题行高 | `var(--kdds-g-font-lineheight-4)` |
| `--kdds-c-card-text-font-size` | 卡片正文文字大小 | `var(--kdds-g-font-scale-3)` |
| `--kdds-c-card-text-font-weight` | 卡片正文字重 | `var(--kdds-g-font-weight-5)` |
| `--kdds-c-card-text-line-height` | 卡片正文行高 | `var(--kdds-g-font-lineheight-5)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-card-border-radius` | 卡片边框圆角 | `0%` |
| `--kdds-c-card-border-width` | 卡片边框宽度 | `var(--kdds-g-sizing-border-1)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-card-header-padding-horizontal` | 卡片头部区域左右内边距 | `var(--kdds-g-spacing-6)` |
| `--kdds-c-card-header-padding-vertical` | 卡片头部区域上下内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-card-icon-margin-right` | 卡片图标右外边距 | `var(--kdds-g-spacing-2)` |
| `--kdds-c-card-body-padding-horizontal` | 卡片主体区域左右内边距 | `var(--kdds-g-spacing-6)` |
| `--kdds-c-card-body-padding-top` | 卡片主体区域上内边距 | `var(--kdds-g-spacing-4)` |
| `--kdds-c-card-body-padding-bottom` | 卡片主体区域下内边距 | `var(--kdds-g-spacing-6)` |
| `--kdds-c-card-footer-padding-horizontal` | 卡片底部区域左右内边距 | `var(--kdds-g-spacing-6)` |

## 使用card默认插槽示例代码：
```html
### ✅ [正确写法 - Good Case]
*说明：主体内容直接放在标签内，无需 slot 属性。*
<kd-card  title="Hello">
    <kd-button label="New" slot="actions"></kd-button>
    <p class="kdds-card-body">Card Body (custom component)</p>
    <p slot="footer">Card Footer</p>
</kd-card>
```
### ❌ [错误写法 - Bad Case - 禁止生成]
说明：不要显式声明 default 插槽，这是 KWC 不支持的语法。

```html
<kd-card  title="Hello">
    <kd-button label="New" slot="actions"></kd-button>
    <p slot="default" class="kdds-card-body">Card Body (custom component)</p>
    <p slot="footer">Card Footer</p>
</kd-card>
```

## card 默认用法
```html
<kd-card title="Hello">
    <div slot="actions">This is card header</div>
    <p class="kdds-card-body">Card Body Narrow (custom component)</p>
    <p slot="footer">Card Footer</p>
</kd-card>
```

## card 自定义header和footer
```html
<kd-card>
    <h3 slot="title">
        <kd-icon icon-name="icon-font-loading"></kd-icon>
        Card Title
    </h3>
    <div slot="footer">
            <kd-button>confirm</kd-button>
            <kd-button>cancel</kd-button>
    </div>
    <p class="kdds-card-body">Card Body (custom component)</p>
</kd-card>
```

## 使用card 提供的token实现自定义样式示例代码：
1. 先在kd-card中定义类名
```html
<kd-card  title="Hello" class="kdds-custom-card">
    <kd-button label="New" slot="actions"></kd-button>
    <p class="kdds-card-body">Card Body (custom component)</p>
    <p slot="footer">Card Footer</p>
</kd-card>
```

2. 在css文件中使用kd-card提供的token实现定制化样式
```css
.kdds-custom-card {
  --kdds-c-card-background: #ff0000;
}
```