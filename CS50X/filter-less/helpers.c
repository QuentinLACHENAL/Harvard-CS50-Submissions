#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            average =
                roundf((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            // Update pixel values
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float originalBlue = image[i][j].rgbtBlue;
            float originalGreen = image[i][j].rgbtGreen;
            float originalRed = image[i][j].rgbtRed;
            // new values
            float newBlue = roundf(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);
            float newGreen =
                roundf(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            float newRed = roundf(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            // if > 255 needs to be = 255
            if (newBlue > 255)
                newBlue = 255;
            if (newGreen > 255)
                newGreen = 255;
            if (newRed > 255)
                newRed = 255;

            // Update pixel values
            image[i][j].rgbtBlue = newBlue;
            image[i][j].rgbtGreen = newGreen;
            image[i][j].rgbtRed = newRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blur_value_red = 0;
            int blur_value_green = 0;
            int blur_value_blue = 0;
            int count_additions = 0;

            for (int k = i - 1; k <= i + 1; k++)
            {
                if (k < 0 || k >= height)
                    continue;
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if (l < 0 || l >= width)
                        continue;
                    blur_value_red += copy[k][l].rgbtRed;
                    blur_value_green += copy[k][l].rgbtGreen;
                    blur_value_blue += copy[k][l].rgbtBlue;
                    count_additions++;
                }
            }
            image[i][j].rgbtRed = roundf((float) blur_value_red / count_additions);
            image[i][j].rgbtGreen = roundf((float) blur_value_green / count_additions);
            image[i][j].rgbtBlue = roundf((float) blur_value_blue / count_additions);
        }
    }
    return;
}
