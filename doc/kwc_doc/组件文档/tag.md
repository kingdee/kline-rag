# 🏷️ Tag 标签

- 组件名: `kd-tag`
- 说明: 标签（Tag）是一种对事物进行标记和分类的组件。

---

## 🛠️ API 属性

以下表格描述了标签组件的属性、类型、默认值及引入版本。

| 属性 | 说明 | 类型 | 默认值 | 版本 |
| :--- | :--- | :--- | :--- | :--- |
| `label` | 标签内显示的文本内容 | `string` | - | 1.0.0 |
| `prefix-icon` | 前缀图标 | `string` | - | 1.0.0 |
| `suffix-icon` | 后缀图标 | `string` | - | 1.0.0 |
| `shape` | 标签的形状，可选值包括 `round`、`square` 和 `mark` | `string` | `round` | 1.0.0 |
| `state` | 标签的状态，可选值包括 `default`、`invalid`、`success`、`processing`、`warning` 和 `error` | `string` | `default` | 1.0.0 |
| `variant` | 标签的视觉样式变体。可选值包括 `dark`、`light`、`outlined`、`light-outlined` 和 `text` | `string` | `light-outlined` | 1.0.0 |
| `size` | 标签的尺寸，可选值包括 `large`、`medium` 和 `small` | `string` | `small` | 1.0.0 |
| `max-width` | 标签的最大宽度，超过此宽度的内容将被截断并显示省略号（...） | `string` | - | 1.0.0 |
| `closable` | 设置标签是否可关闭 | `boolean` | `FALSE` | 1.0.0 |
| `onclose` | 如果关闭按钮存在，点击关闭按钮时触发 | - | - | 1.0.0 |

---

## 🎨 设计变量 (Design Tokens)

以下表格描述了标签组件所使用的所有设计变量。

### 颜色 (Color) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `--kdds-c-tag-dark-color` | 暗色模式下的标签文字颜色 | `var(--kdds-g-color-neutral-base-100,#FFFFFF)` |
| `--kdds-c-tag-dark-background-default` | 暗色模式下载签默认背景颜色 | `var(--kdds-g-color-neutral-base-25,#404040)` |
| `--kdds-c-tag-dark-background-success` | 暗色模式下载签成功状态背景颜色 | `var(--kdds-g-color-on-success-1,#1BA854)` |
| `--kdds-c-tag-dark-background-processing` | 暗色模式下载签处理中状态背景颜色 | `var(--kdds-g-color-on-info-1,#276FF5)` |
| `--kdds-c-tag-dark-background-warning` | 暗色模式下载签警告状态背景颜色 | `var(--kdds-g-color-on-warning-1,#FF991C)` |
| `--kdds-c-tag-dark-background-error` | 暗色模式下载签错误状态背景颜色 | `var(--kdds-g-color-on-error-1,#FB2323)` |
| `--kdds-c-tag-dark-background-invalid` | 暗色模式下载签禁用状态背景颜色 | `var(--kdds-g-color-on-disabled-1,#B2B2B2)` |
| `--kdds-c-tag-outlined-background` | 描边标签背景颜色（透明） | `transparent` |
| `--kdds-c-tag-outlined-color-default` | 描边标签默认文字颜色 | `var(--kdds-g-color-neutral-base-25,#404040)` |
| `--kdds-c-tag-outlined-border-default` | 描边标签默认边框颜色 | `var(--kdds-g-color-neutral-base-25,#404040)` |
| `--kdds-c-tag-outlined-color-success` | 描边标签成功状态文字颜色 | `var(--kdds-g-color-success-1,#1BA854)` |
| `--kdds-c-tag-outlined-border-success` | 描边标签成功状态边框颜色 | `var(--kdds-g-color-success-1,#1BA854)` |
| `--kdds-c-tag-outlined-color-processing` | 描边标签处理中状态文字颜色 | `var(--kdds-g-color-info-1,#276FF5)` |
| `--kdds-c-tag-outlined-border-processing` | 描边标签处理中状态边框颜色 | `var(--kdds-g-color-info-1,#276FF5)` |
| `--kdds-c-tag-outlined-color-warning` | 描边标签警告状态文字颜色 | `var(--kdds-g-color-warning-1,#FF991C)` |
| `--kdds-c-tag-outlined-border-warning` | 描边标签警告状态边框颜色 | `var(--kdds-g-color-warning-1,#FF991C)` |
| `--kdds-c-tag-outlined-color-error` | 描边标签错误状态文字颜色 | `var(--kdds-g-color-error-1,#FB2323)` |
| `--kdds-c-tag-outlined-border-error` | 描边标签错误状态边框颜色 | `var(--kdds-g-color-error-1,#FB2323)` |
| `--kdds-c-tag-outlined-color-invalid` | 描边标签禁用状态文字颜色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-tag-outlined-border-invalid` | 描边标签禁用状态边框颜色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-tag-light-background-default` | 亮色模式下载签默认背景颜色 | `var(--kdds-g-color-neutral-base-96,#F5F5F5)` |
| `--kdds-c-tag-light-color-default` | 亮色模式下载签默认文字颜色 | `var(--kdds-g-color-neutral-base-25,#404040)` |
| `--kdds-c-tag-light-background-success` | 亮色模式下载签成功状态背景颜色 | `var(--kdds-g-color-success-container-2,#DCFAE4)` |
| `--kdds-c-tag-light-color-success` | 亮色模式下载签成功状态文字颜色 | `var(--kdds-g-color-success-1,#1BA854)` |
| `--kdds-c-tag-light-background-processing` | 亮色模式下载签处理中状态背景颜色 | `var(--kdds-g-color-info-container-1,#E0EFFF)` |
| `--kdds-c-tag-light-color-processing` | 亮色模式下载签处理中状态文字颜色 | `var(--kdds-g-color-info-1,#276FF5)` |
| `--kdds-c-tag-light-background-warning` | 亮色模式下载签警告状态背景颜色 | `var(--kdds-g-color-warning-container-1,#FFF1D4)` |
| `--kdds-c-tag-light-color-warning` | 亮色模式下载签警告状态文字颜色 | `var(--kdds-g-color-warning-1,#FF991C)` |
| `--kdds-c-tag-light-background-error` | 亮色模式下载签错误状态背景颜色 | `var(--kdds-g-color-error-container-1,#FFDBE0)` |
| `--kdds-c-tag-light-color-error` | 亮色模式下载签错误状态文字颜色 | `var(--kdds-g-color-error-1,#FB2323)` |
| `--kdds-c-tag-light-background-invalid` | 亮色模式下载签禁用状态背景颜色 | `var(--kdds-g-color-disabled-container-1,#F5F5F5)` |
| `--kdds-c-tag-light-color-invalid` | 亮色模式下载签禁用状态文字颜色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-tag-light-outlined-background-default` | 亮色描边标签默认背景颜色 | `var(--kdds-g-color-neutral-base-96,#F5F5F5)` |
| `--kdds-c-tag-light-outlined-color-default` | 亮色描边标签默认文字颜色 | `var(--kdds-g-color-neutral-base-25,#404040)` |
| `--kdds-c-tag-light-outlined-border-default` | 亮色描边标签默认边框颜色 | `var(--kdds-g-color-neutral-base-85,#D9D9D9)` |
| `--kdds-c-tag-light-outlined-background-success` | 亮色描边标签成功状态背景颜色 | `var(--kdds-g-color-success-container-2,#F2FFF5)` |
| `--kdds-c-tag-light-outlined-color-success` | 亮色描边标签成功状态文字颜色 | `var(--kdds-g-color-success-1,#1BA854)` |
| `--kdds-c-tag-light-outlined-border-success` | 亮色描边标签成功状态边框颜色 | `var(--kdds-g-color-border-success-2,#DCFAE4)` |
| `--kdds-c-tag-light-outlined-background-processing` | 亮色描边标签处理中状态背景颜色 | `var(--kdds-g-color-info-container-2,#F2F9FF)` |
| `--kdds-c-tag-light-outlined-color-processing` | 亮色描边标签处理中状态文字颜色 | `var(--kdds-g-color-info-1,#276FF5)` |
| `--kdds-c-tag-light-outlined-border-processing` | 亮色描边标签处理中状态边框颜色 | `var(--kdds-g-color-border-info-2,#E0EFFF)` |
| `--kdds-c-tag-light-outlined-background-warning` | 亮色描边标签警告状态背景颜色 | `var(--kdds-g-color-warning-container-2,#FFFBF2)` |
| `--kdds-c-tag-light-outlined-color-warning` | 亮色描边标签警告状态文字颜色 | `var(--kdds-g-color-warning-1,#FF991C)` |
| `--kdds-c-tag-light-outlined-border-warning` | 亮色描边标签警告状态边框颜色 | `var(--kdds-g-color-border-warning-2,#FFF1D4)` |
| `--kdds-c-tag-light-outlined-background-error` | 亮色描边标签错误状态背景颜色 | `var(--kdds-g-color-error-container-2,#FFF2F4)` |
| `--kdds-c-tag-light-outlined-color-error` | 亮色描边标签错误状态文字颜色 | `var(--kdds-g-color-error-1,#FB2323)` |
| `--kdds-c-tag-light-outlined-border-error` | 亮色描边标签错误状态边框颜色 | `var(--kdds-g-color-border-error-2,#FFDBE0)` |
| `--kdds-c-tag-light-outlined-background-invalid` | 亮色描边标签禁用状态背景颜色 | `var(--kdds-g-color-disabled-container-1,#F5F5F5)` |
| `--kdds-c-tag-light-outlined-color-invalid` | 亮色描边标签禁用状态文字颜色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-tag-light-outlined-border-invalid` | 亮色描边标签禁用状态边框颜色 | `var(--kdds-g-color-border-disabled-1,#D9D9D9)` |
| `--kdds-c-tag-text-color-default` | 文本标签默认文字颜色 | `var(--kdds-g-color-neutral-base-25,#404040)` |
| `--kdds-c-tag-text-color-success` | 文本标签成功状态文字颜色 | `var(--kdds-g-color-success-1,#1BA854)` |
| `--kdds-c-tag-text-color-processing` | 文本标签处理中状态文字颜色 | `var(--kdds-g-color-info-1,#276FF5)` |
| `--kdds-c-tag-text-color-warning` | 文本标签警告状态文字颜色 | `var(--kdds-g-color-warning-1,#FF991C)` |
| `--kdds-c-tag-text-color-error` | 文本标签错误状态文字颜色 | `var(--kdds-g-color-error-1,#FB2323)` |
| `--kdds-c-tag-text-color-invalid` | 文本标签禁用状态文字颜色 | `var(--kdds-g-color-disabled-1,#B2B2B2)` |
| `--kdds-c-tag-close-color-default-hover` | 关闭按钮默认悬停颜色 | `var(--kdds-g-color-neutral-base-60,#999999)` |
| `--kdds-c-tag-close-color-success-hover` | 关闭按钮成功状态悬停颜色 | `var(--kdds-g-color-success-base-60,#40BD6E)` |
| `--kdds-c-tag-close-color-processing-hover` | 关闭按钮处理中状态悬停颜色 | `var(--kdds-g-color-info-base-60,#5797FF)` |
| `--kdds-c-tag-close-color-warning-hover` | 关闭按钮警告状态悬停颜色 | `var(--kdds-g-color-warning-base-60,#FFB44A)` |
| `--kdds-c-tag-close-color-error-hover` | 关闭按钮错误状态悬停颜色 | `var(--kdds-g-color-error-base-60,#FF5257)` |
| `--kdds-c-tag-close-color-invalid-hover` | 关闭按钮禁用状态悬停颜色 | `var(--kdds-g-color-neutral-base-85,#D9D9D9)` |
| `--kdds-c-tag-close-color-default-active` | 关闭按钮默认激活颜色 | `var(--kdds-g-color-neutral-base-18,#2F2F2F)` |
| `--kdds-c-tag-close-color-success-active` | 关闭按钮成功状态激活颜色 | `var(--kdds-g-color-success-base-40,#0A803D)` |
| `--kdds-c-tag-close-color-processing-active` | 关闭按钮处理中状态激活颜色 | `var(--kdds-g-color-success-base-40,#104CCC)` |
| `--kdds-c-tag-close-color-warning-active` | 关闭按钮警告状态激活颜色 | `var(--kdds-g-color-warning-base-40,#D67206)` |
| `--kdds-c-tag-close-color-error-active` | 关闭按钮错误状态激活颜色 | `var(--kdds-g-color-error-base-40,#D1130D)` |
| `--kdds-c-tag-close-color-invalid-active` | 关闭按钮禁用状态激活颜色 | `var(--kdds-g-color-neutral-base-60,#999999)` |
| `--kdds-c-tag-dark-close-color` | 暗色模式关闭按钮颜色 | `var(--kdds-g-color-neutral-base-100,#FFFFFF)` |
| `--kdds-c-tag-dark-close-color-hover` | 暗色模式关闭按钮悬停颜色 | `var(--kdds-g-color-neutral-base-100,#FFFFFF) var(--kdds-g-opacity-60,65%)` |
| `--kdds-c-tag-dark-close-color-active` | 暗色模式关闭按钮激活颜色 | `var(--kdds-g-color-neutral-base-100,#FFFFFF)` |

### 排版 (Typography) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `Typography--kdds-c-tag-line-height-small` | 标签小尺寸的行高 | `var(--kdds-g-font-lineheight-4,1.5)` |
| `Typography--kdds-c-tag-line-height-medium` | 标签中尺寸的行高 | `var(--kdds-g-font-lineheight-5,1.572)` |
| `Typography--kdds-c-tag-line-height-large` | 标签大尺寸的行高 | `var(--kdds-g-font-lineheight-4,1.5)` |
| `Typography--kdds-c-tag-font-size-small` | 标签小尺寸的字体大小 | `var(--kdds-g-font-scale-2,0.75rem)` |
| `Typography--kdds-c-tag-font-size-medium` | 标签中尺寸的字体大小 | `var(--kdds-g-font-scale-3,0.875rem)` |
| `Typography--kdds-c-tag-font-size-large` | 标签大尺寸的字体大小 | `var(--kdds-g-font-scale-4,1rem)` |
| `Typography--kdds-c-tag--close-font-size-large` | 大尺寸关闭按钮的字体大小 | `var(--kdds-g-icon-sizing-2,0.75rem)` |
| `Typography--kdds-c-tag--close-font-size-medium` | 中尺寸关闭按钮的字体大小 | `var(--kdds-g-icon-sizing-3,1rem)` |
| `Typography--kdds-c-tag--close-font-size-small` | 小尺寸关闭按钮的字体大小 | `var(--kdds-g-icon-sizing-4,1.25rem)` |

### 间距 (Spacing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `Spacing--kdds-c-tag-padding-left-small` | 标签小尺寸的左内边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `Spacing--kdds-c-tag-padding-right-small` | 标签小尺寸的右内边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `Spacing--kdds-c-tag-padding-top-small` | 标签小尺寸的上内边距 | `calc(var(--kdds-g-spacing-1,0.125rem)-2px)` |
| `Spacing--kdds-c-tag-padding-bottom-small` | 标签小尺寸的下内边距 | `calc(var(--kdds-g-spacing-1,0.125rem)-2px)` |
| `Spacing--kdds-c-tag-padding-left-medium` | 标签中尺寸的左内边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `Spacing--kdds-c-tag-padding-right-medium` | 标签中尺寸的右内边距 | `var(--kdds-g-spacing-4,0.5rem)` |
| `Spacing--kdds-c-tag-padding-top-medium` | 标签中尺寸的上内边距 | `calc(var(--kdds-g-spacing-1,0.125rem)-1px)` |
| `Spacing--kdds-c-tag-padding-bottom-medium` | 标签中尺寸的下内边距 | `calc(var(--kdds-g-spacing-1,0.125rem)-1px)` |
| `Spacing--kdds-c-tag-padding-left-large` | 标签大尺寸的左内边距 | `var(--kdds-g-spacing-5,0.75rem)` |
| `Spacing--kdds-c-tag-padding-right-large` | 标签大尺寸的右内边距 | `var(--kdds-g-spacing-5,0.75rem)` |
| `Spacing--kdds-c-tag-padding-top-large` | 标签大尺寸的上内边距 | `calc(var(--kdds-g-spacing-1,0.125rem)+1px)` |
| `Spacing--kdds-c-tag-padding-bottom-large` | 标签大尺寸的下内边距 | `calc(var(--kdds-g-spacing-1,0.125rem)+1px)` |
| `Spacing--kdds-c-tag-prefixicon-margin-right` | 前缀图标右外边距 | `var(--kdds-g-spacing-2,0.25rem)` |
| `Spacing--kdds-c-tag-suffixicon-margin-left` | 后缀图标左外边距 | `var(--kdds-g-spacing-2,0.25rem)` |
| `Spacing--kdds-c-tag-close-margin-left` | 关闭按钮左外边距 | `var(--kdds-g-spacing-4,0.5rem)` |

### 边框 (Border) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `Border--kdds-c-tag-border-width` | 标签边框宽度 | `var(--kdds-g-sizing-border-1,1px)` |
| `Border--kdds-c-tag-shape-square-border-radius` | 方形标签的边框圆角 | `var(--kdds-g-radius-border-1,0.125rem)` |
| `Border--kdds-c-tag-shape-round-border-radius` | 圆形标签的边框圆角 | `var(--kdds-g-radius-border-circle,100%)` |
| `Border--kdds-c-tag-shape-mark-border-radius` | 标记标签的边框圆角（多个值） | `var(--kdds-g-radius-border-1,0.125rem),var(--kdds-g-radius-border-circle,100%),var(--kdds-g-radius-border-1,0.125rem),var(--kdds-g-radius-border-circle,100%)` |

### 尺寸 (Sizing) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `Sizing--kdds-c-tag-sizing-min-width-small` | 标签小尺寸的最小宽度 | `28px` |
| `Sizing--kdds-c-tag-sizing-min-width-medium` | 标签中尺寸的最小宽度 | `30px` |
| `Sizing--kdds-c-tag-sizing-min-width-large` | 标签大尺寸的最小宽度 | `40px` |

### 透明度 (Opacity) 变量

| Token 名称 | 说明 | 默认值 |
| :--- | :--- | :--- |
| `Opacity--kdds-c-tag-custom-close-opacity` | 关闭按钮默认透明度 | `var(--kdds-g-opacity-100,1)` |
| `Opacity--kdds-c-tag-custom-close-opacity-hover` | 关闭按钮悬停时透明度 | `var(--kdds-g-opacity-60,0.6)` |
| `Opacity--kdds-c-tag-custom-close-opacity-active` | 关闭按钮激活时透明度 | `var(--kdds-g-opacity-100,1)` |