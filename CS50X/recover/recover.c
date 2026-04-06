#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
        return 1;
    // Open the memory card
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
        return 1;

    uint8_t buffer[512];
    int i = 0;
    char filename[8];
    FILE *img = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, f) == 512)
    {

        // Create JPEGs from the data

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
                fclose(img);

            sprintf(filename, "%03i.jpg", i++);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                fclose(f);
                return 1;
            }
        }
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    if (img != NULL)
        fclose(img);
    fclose(f);

    return 0;
}
