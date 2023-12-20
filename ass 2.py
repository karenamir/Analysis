def sequence_alignment(x, y, scoring_matrix):
    n = len(x)
    m = len(y)


    dp = [[0] * (m + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]
            delete = dp[i - 1][j] + scoring_matrix[x[i - 1]]['-']
            insert = dp[i][j - 1] + scoring_matrix['-'][y[j - 1]]
            dp[i][j] = max(match, delete, insert)

 
    align_x, align_y = '', ''
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]:
            align_x = x[i - 1] + align_x
            align_y = y[j - 1] + align_y
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + scoring_matrix[x[i - 1]]['-']:
            align_x = x[i - 1] + align_x
            align_y = '-' + align_y
            i -= 1
        else:
            align_x = '-' + align_x
            align_y = y[j - 1] + align_y
            j -= 1

    return align_x, align_y


x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': float('inf')}
}


alignment_result = sequence_alignment(x, y, scoring_matrix)


print("Alignment:")
print(alignment_result[0])
print(alignment_result[1])
