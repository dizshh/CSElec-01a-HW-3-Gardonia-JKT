# CSElec-01a-HW-3-Gardonia-JKT

<img width="798" height="911" alt="image" src="https://github.com/user-attachments/assets/8176d671-ce49-4d03-a32a-8fac1a940bfe" />

<img width="762" height="61" alt="image" src="https://github.com/user-attachments/assets/6cdf5210-c3c7-4c0d-88cb-5bb375e232cc" />

Graph:

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/72730e01-13d3-42fe-9785-904de17600cc" />


Truncated pi is better for this experiment. Here's why:

Graph 4 (Percentage Error) is the key:

Truncated Pi error (blue) stays extremely low and decreases as precision increases — it converges toward the true value
Rounded Pi (3.1416) error (coral) remains constant at the same high level across all precisions because it's always padded with zeros, never gaining accuracy
Graph 3 (Difference Between Methods) shows the gap between the two approaches growing — this confirms that truncated pi is getting more accurate while rounded pi stays frozen at 4 decimal places.

Graph 2 (Surface Area) shows the truncated pi bars aligning closely with the true surface area line (green dashed), while the rounded pi consistently overshoots.

The verdict:

Using more digits of pi (truncation approach) gives increasingly accurate surface area calculations
The fixed "school pi" (3.1416) introduces a constant ~0.0013% error that never improves regardless of how many decimal places you work with
