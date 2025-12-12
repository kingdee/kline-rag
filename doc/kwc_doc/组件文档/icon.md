# ✨ Icon 图标

- 组件名: `kd-icon`
- 说明: 图标（Icon）是语义化的矢量图形组件。

---

## 🛠️ API 属性

以下表格描述了图标组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `icon-name` | 图标名称 | - | - | 1.0.0 |
| `spin` | 是否开启**旋转动画效果** | `boolean` | `FALSE` | 1.0.0 |
| `onclick` | 点击时触发的事件 | - | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了图标组件所使用的设计变量。

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-icon-font-size` | 图标大小 | `var(--kdds-g-icon-sizing-3,1rem)` |

## 代码示例
```html
<!-- 图标基本用法 -->
<kd-icon icon-name="kdfont-GIT"></kd-icon>
<kd-icon icon-name="kdfont-GPT4"></kd-icon>
<kd-icon icon-name="kdfont-GPTzhushou"></kd-icon>
<kd-icon icon-name="kdfont-JS-mianxing-yidong"></kd-icon>
<!-- 给图标添加旋转效果 -->
<kd-icon icon-name="kdfont-JS2" spin></kd-icon>
<!-- 给图标添加点击事件 -->
<kd-icon icon-name="kdfont-PDF2" spin onclick={handleClick}></kd-icon>
```