def parse(source_code, max_line_length):
    is_block_comment = False
    result = {
        'parenthesis_open': 0,
        'parenthesis_close': 0,
        'tab': [],
        'whitespace': [],
        'line_length': [],
    }
    for i, line in enumerate(source_code.splitlines()):
        line_num = i + 1
        if line.startswith('#|'):
            is_block_comment = True
        elif line.startswith('|#'):
            is_block_comment = False
        if is_block_comment:
            continue
        is_beginning = True
        is_line_comment = False
        is_inline_comment = False
        has_quote = False
        in_quote = False
        whitespace = 0
        for char in line:
            if char == ';':
                if in_quote is False:
                    if is_beginning:
                        is_line_comment = True
                    else:
                        is_inline_comment = True
                    break
            if char == ' ':
                if is_beginning is not True:
                    whitespace += 1
            else:
                if is_beginning:
                    is_beginning = False
            if char == '(':
                result['parenthesis_open'] += 1
            if char == ')':
                result['parenthesis_close'] += 1
            if char == '"':
                in_quote = not in_quote
                has_quote = True
            if char == '\t':
                result['tab'].append(line_num)
        is_comment = is_line_comment or is_inline_comment
        if len(line.split()) != 0 and is_comment is not True \
           and has_quote is not True and whitespace != len(line.split())-1:
            result['whitespace'].append(line_num)
        if is_line_comment is not True \
           and has_quote is not True and len(line) > max_line_length:
            result['line_length'].append([line_num, len(line)])
    return result
