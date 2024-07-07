% Define the observed data as a contingency table
observed_data = [37,34;31,39;27,40;29,41;34,46];
%observed_data = [19,21,27,24,27,22,15,15,16;9,11,7,7,12,11,9,10,9;6,10,9,10,9,12,9,9,10;9,8,8,10,9,6,8,7,7;27,30,19,23,18,25,31,31,28;11,7,9,7,9,8,9,8,10;6,2,8,8,13,9,9,9,10;4,4,5,5,6,4,3,3,4;4,4,4,3,4,5,5,5,3;4,2,4,2,1,4,2,3,3];
% Calculate the row and column sums
row_sums = sum(observed_data, 2);
col_sums = sum(observed_data, 1);

% Calculate the total sum of the observed data
total_sum = sum(row_sums);

% Calculate the expected frequencies based on the assumption of independence
expected_data = row_sums * col_sums / total_sum;

% Calculate the chi-square statistic
chi_squared = sum(sum((observed_data - expected_data).^2 ./ expected_data));

% Determine the degrees of freedom
degrees_of_freedom = (size(observed_data, 1) - 1) * (size(observed_data, 2) - 1);

% Calculate the p-value using the chi-square distribution
p_value = 1 - chi2cdf(chi_squared, degrees_of_freedom);

% Display the results
disp(['Chi-square statistic: ' num2str(chi_squared)]);
disp(['Degrees of freedom: ' num2str(degrees_of_freedom)]);
disp(['p-value: ' num2str(p_value)]);