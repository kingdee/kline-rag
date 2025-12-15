# LWC Layout 对齐和间距示例

## 组件说明
`kd-layout` 组件提供了多种属性来控制布局项的对齐方式和间距。通过这些属性，开发者可以精确控制布局的视觉效果，创建更加专业和美观的界面。

## 带对齐和间距的布局示例

```html
<!-- alignmentSpacingLayoutExample.html -->
<template>
    <kd-layout
        horizontal-align="center"
        vertical-align="stretch"
        multiple-rows>
        
        <!-- 对齐的内容 -->
        <kd-layout-item size="12" sm="6" lg="3">
            <div >
                <h3>Aligned Item 1</h3>
                <p>Centered horizontally, stretched vertically</p>
            </div>
        </kd-layout-item>
        
        <kd-layout-item size="12" sm="6" lg="3">
            <div >
                <h3>Aligned Item 2</h3>
                <p>Centered horizontally, stretched vertically</p>
                <p>This item has more content than the others, causing all items to stretch to match its height.</p>
            </div>
        </kd-layout-item>
        
        <kd-layout-item size="12" sm="6" lg="3">
            <div >
                <h3>Aligned Item 3</h3>
                <p>Centered horizontally, stretched vertically</p>
            </div>
        </kd-layout-item>
        
        <kd-layout-item size="12" sm="6" lg="3">
            <div >
                <h3>Aligned Item 4</h3>
                <p>Centered horizontally, stretched vertically</p>
            </div>
        </kd-layout-item>
    </kd-layout>
    
    <!-- 不同对齐方式的示例 -->
    <div >
        <h3>不同对齐方式示例</h3>
        
        <!-- 左对齐 -->
        <kd-layout horizontal-align="start" multiple-rows>
            <kd-layout-item size="4">
                <div >
                    <p>Left Aligned</p>
                </div>
            </kd-layout-item>
            <kd-layout-item size="4">
                <div >
                    <p>Left Aligned</p>
                </div>
            </kd-layout-item>
        </kd-layout>
        
        <!-- 右对齐 -->
        <kd-layout horizontal-align="end" multiple-rows >
            <kd-layout-item size="4">
                <div >
                    <p>Right Aligned</p>
                </div>
            </kd-layout-item>
            <kd-layout-item size="4">
                <div >
                    <p>Right Aligned</p>
                </div>
            </kd-layout-item>
        </kd-layout>
        
        <!-- 两端对齐 -->
        <kd-layout horizontal-align="space-between" multiple-rows >
            <kd-layout-item size="4">
                <div >
                    <p>Space Between</p>
                </div>
            </kd-layout-item>
            <kd-layout-item size="4">
                <div >
                    <p>Space Between</p>
                </div>
            </kd-layout-item>
        </kd-layout>
    </div>
</template>
```

## 示例说明

### 核心属性
- **horizontal-align**: 控制布局项的水平对齐方式
  - `start`: 左对齐
  - `center`: 居中对齐
  - `end`: 右对齐
  - `space-around`: 均匀分布，两端留白
  - `space-between`: 两端对齐，中间均匀分布

- **vertical-align**: 控制布局项的垂直对齐方式
  - `top`: 顶部对齐
  - `center`: 居中对齐
  - `stretch`: 拉伸对齐，所有项高度相同



### 对齐效果
1. **水平居中对齐**: 通过 `horizontal-align="center"` 实现
2. **垂直拉伸对齐**: 通过 `vertical-align="stretch"` 实现，所有布局项高度相同

## 使用场景
- 卡片网格布局
- 产品展示网格

## 代码结构
```
alignmentSpacingLayoutExample/
├── alignmentSpacingLayoutExample.html  # 组件模板
├── alignmentSpacingLayoutExample.js    # 组件逻辑（可选）
└── alignmentSpacingLayoutExample.css  # 组件样式
```

## 最佳实践
- 使用 `vertical-align="stretch"` 实现等高布局
- 根据内容选择合适的对齐方式
- 测试不同屏幕尺寸下的对齐效果

## 注意事项
- `vertical-align="stretch"` 只有在布局项内容高度不同时才会明显生效
- 对齐属性会影响整个布局，而不是单个布局项
