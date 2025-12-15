# LWC Layout 组件基本用法示例

## 组件说明
`kd-layout` 和 `kd-layout-item` 是 KWC 中用于创建响应式布局的核心组件。它们基于 CSS 
- Flexbox 实现，提供了简单易用的属性来控制布局的行为和外观。
- kd-layout下面必须使用kd-layout-item组件，kd-layout-item组件下面可以放置任意内容。

## 基本用法示例

```html
<!-- layoutBasicExample.html -->
<template>
    <kd-layout>
        <kd-layout-item>
            <!-- 第一个布局项内容 -->
            <div >
                <h3>First Item</h3>
                <p>This is the content of the first layout item.</p>
            </div>
        </kd-layout-item>
        <kd-layout-item>
            <!-- 第二个布局项内容 -->
            <div >
                <h3>Second Item</h3>
                <p>This is the content of the second layout item.</p>
            </div>
        </kd-layout-item>
    </kd-layout>
</template>
```

### 组件结构
- 使用 `<kd-layout>` 作为布局容器
- `<kd-layout>`内添加多个 `<kd-layout-item>` 作为布局项
- 每个布局项内部可以包含任意内容，这里使用了带有内边距的 `div` 来包裹内容

### 特点
- 布局项不会自动换行，需要添加 `multiple-rows` 属性才能实现换行
- 适合创建简单的两列或多列布局

## 使用场景
- 简单的两列内容展示
- 基本的卡片布局

## 代码结构
```
layoutBasicExample/
├── layoutBasicExample.html  # 组件模板
├── layoutBasicExample.js    # 组件逻辑（可选）
└── layoutBasicExample.css  # 组件样式
```

## 注意事项
- 当布局项内容超过容器宽度时，会出现横向滚动条
- 可以通过添加 `size` 属性来控制布局项的宽度
- 适合响应式设计，能够在不同屏幕尺寸下自动调整布局
