public static StringBuilder doReduc(StringBuilder strBuilder) {
    StringBuilder sb = new StringBuilder();
    if (strBuilder != null && strBuilder.length() != 0) {
        strBuilder.append(" ");
        // 是否有相临相同匹配
        boolean same = false;
        // 相临相同匹配首字符
        char c = strBuilder.charAt(0);
        for (int i = 1; i < strBuilder.length(); i++) {
            if (c == strBuilder.charAt(i)) {
                same = true;
            } else {
                if (!same) {
                    sb.append(c);
                }
                c = strBuilder.charAt(i);
                same = false;
            }
        }
        // 匹配完成，如果字符串长度没变则说明没有需要继续消除的了，否则递归继续消除
        if (sb.length() + 1 < strBuilder.length()) {
            return doReduce(sb);
        }
    }
    return sb;
}

