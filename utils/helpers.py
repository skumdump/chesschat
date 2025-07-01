def truncate(text, max_length):
    '''Truncate long text with ellipsis.'''
    return text if len(text) <= max_length else text[:max_length - 3] + '...'