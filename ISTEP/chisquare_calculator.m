observed = [6, 11, 9, 6, 27, 4, 4, 9, 4, 19];  % Observed frequencies
expected = [10, 8, 11, 7, 24, 5, 5, 10, 2, 18];  % Expected frequencies (under null hypothesis)

% Calculate the chi-square test statistic
chi2 = sum((observed - expected).^2 ./ expected);

% Determine the degrees of freedom
df = numel(observed) - 1;

% Lookup the critical value at the desired significance level (e.g., 0.05)
alpha = 0.01;
critical_value = chi2inv(1 - alpha, df);

% Calculate the p-value
p_value = 1 - chi2cdf(chi2, df);

% Display the results
disp(['Chi-square value: ' num2str(chi2)]);
disp(['Degrees of freedom: ' num2str(df)]);
disp(['Critical value: ' num2str(critical_value)]);
disp(['P-value: ' num2str(p_value)]);

% Check the test result
if chi2 >= critical_value
    disp('The observed data significantly deviates from the expected distribution.');
else
    disp('The observed data does not significantly deviate from the expected distribution.');
end