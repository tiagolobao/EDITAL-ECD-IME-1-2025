install.packages("ggplot2")
library(ggplot2)

# Create the same plot with ggplot2
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point(size = 3, 
             alpha = 0.7,        # Transparency
             color = "darkblue") +
  geom_smooth(method = "lm", 
              color = "red", 
              linetype = "dashed",
              se = FALSE) +      # Remove confidence interval
  labs(title = "Car Weight vs. Fuel Efficiency",
       subtitle = "Motor Trend Car Road Tests (1974)",
       x = "Weight (1000 lbs)",
       y = "Miles per Gallon (MPG)",
       caption = "Source: mtcars dataset") +
  theme_minimal() +              # Clean theme
  theme(plot.title = element_text(face = "bold", size = 14),
        axis.title = element_text(face = "bold"),
        panel.grid.minor = element_blank())