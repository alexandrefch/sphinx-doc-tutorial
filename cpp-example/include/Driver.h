/** @file */

/**
 * @class Driver
 * @brief Driver example
 */
class Driver
{
public:
    /**
     * @brief Write byte to a sensor
     *
     * @param[in]  buffer  description of parameter1
     * @return status return the termination status
     */
    int write(unsigned char *buffer);

private:
    bool mIsActive;
};