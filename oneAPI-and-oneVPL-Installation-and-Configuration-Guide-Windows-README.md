# oneAPI and oneVPL Installation and Configuration Guide (Windows)

This guide provides step-by-step instructions for installing and configuring the oneAPI and oneVPL software development tools on Windows, including the installation of supporting software using Python configuration.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Configuration Steps](#configuration-steps)
4. [Testing the Installation](#testing-the-installation)
5. [Additional Resources](#additional-resources)

## Prerequisites

Before proceeding with the installation, ensure that your system meets the following prerequisites:

**Graphics Processors:**

Supported by oneVPL:

- Intel® Iris® Xe graphics
- Intel® Iris® Xe MAX graphics
- Intel® Arc™ Graphics
- Intel Data Center GPU Flex Series
- 11th generation Intel® Core™ processors and newer using integrated graphics

Supported by Intel Media SDK:

- Intel® Server GPU
- 5th to 11th generation Intel Core processors using integrated graphics

**Supported Operating Systems:**

- Windows 10, 11

**Compilers:**

- GNU Compiler Collection (GCC)* version 7.4.0 or newer
- Microsoft* Visual Studio 2019 and newer
- Python installed on your system version 3.6 or newer

Please ensure that your system meets these requirements before proceeding with the installation.

## Installation Steps

1. **Download oneAPI Toolkit:**

   - Visit the [Intel oneAPI download page](https://software.intel.com/content/www/us/en/develop/tools/oneapi/base-toolkit/download.html).
   - Select the appropriate version for Windows and download the installer.

2. **Run the Installer:**

   - Locate the downloaded installer and run it with administrative privileges.
   - Follow the on-screen instructions to proceed with the installation.
   - Select the desired installation location and components to install.

3. **Supporting Software:**

   - During the installation, select and install the necessary supporting software components, such as Intel® Graphics Drivers and Intel® oneAPI Base Toolkit.
   - If prompted to install other required components, follow the on-screen instructions.

4. **Accept License Agreements:**

   - Review the license agreements for the installed components.
   - If you agree, accept the licenses to proceed with the installation.

5. **Installation Completion:**

   - Once the installation process is complete, review the installation summary.
   - Make a note of the installation directory and other relevant information.

## Configuration Steps

After installing the oneAPI Toolkit, perform the following steps to configure the environment:

1. **Set Environment Variables:**

   - Open a command prompt with administrative privileges.
   - Set the following environment variables:
   
     Step 1 `set "INTEL_ROOT=<installation_directory>" `: This command sets the environment variable INTEL_ROOT to the specified <installation_directory>. 
     You need to replace <installation_directory> with the actual directory where you have installed the oneAPI and oneVPL software.
          
     Step 2 `set "PATH=%INTEL_ROOT%\compiler\latest\windows\bin; `and` %INTEL_ROOT%\compiler\latest\windows\redist\intel64\compiler;%PATH%"` :
     This command adds the directories %INTEL_ROOT%\compiler\latest\windows\bin and %INTEL_ROOT%\compiler\latest\windows\redist\intel64\compiler to the existing PATH environment variable. 
     These directories contain the necessary binaries for the Intel Compiler.
     
     Step 3 `set "LIB=%INTEL_ROOT%\compiler\latest\windows\lib\intel64;%LIB%"` : This command adds the directory %INTEL_ROOT%\compiler\latest\windows\lib\intel64 to the existing LIB environment variable.
     This directory contains the necessary libraries for the Intel Compiler.
     
   - Replace `<installation_directory>` with the actual installation directory noted during installation.

2. **Update Path:**

   - Append the following directories to the `PATH` environment variable:
   
     `%INTEL_ROOT%\debugger\latest\windows\bin\intel64` : This path points to the directory where the Intel debugger binaries are located.
     
     `%INTEL_ROOT%\mpi\latest\windows\bin` : This path points to the directory where the Intel MPI (Message Passing Interface) binaries are located.
     
     `%INTEL_ROOT%\tbb\latest\windows\bin\intel64\vc14` : This path points to the directory where the Intel Threading Building Blocks (TBB) binaries are located, specifically for Visual Studio 2015 (vc14).
     
     `%INTEL_ROOT%\oneapi\mkl\latest\bin` : This path points to the directory where the Intel Math Kernel Library (MKL) binaries are located.
     
      Please note that `%INTEL_ROOT%` is used as a placeholder for the actual installation directory, which may vary depending on your system and the version of the oneAPI Toolkit you installed.
     

3. **Verify Configuration:**

   - Open a new command prompt and run the following command to verify the configuration:
   
     ```
     icx --version
     ```

   - If the command displays the installed Intel C++ Compiler version, the configuration is successful.

## Testing the Installation

To test the oneAPI and oneVPL installation, follow these steps:

1. **Build and Run a Sample:**

   - Download the [oneVPL repository](https://github.com/oneapi-src/oneVPL) from GitHub.
   - Navigate to the `oneVPL/examples/` directory.
   - Choose a sample and follow the instructions in the sample's README file to build and run it.

2. **Verify Output:**

   - If the sample runs successfully, it indicates that the oneAPI and oneVPL installation is functioning correctly.

## Additional Resources

For more information and detailed documentation, refer to the following resources:

- [Intel oneAPI documentation](https://software.intel.com/content/www/us/en/develop/documentation/oneapi-dpcpp-cpp-development-guide/top.html)
- [oneVPL GitHub repository](https://github.com/oneapi-src/oneVPL)
- [Intel Developer Zone](https://software.intel.com/)
- [Intel Support Center](https://www.intel.com/content/www/us/en/support.html)

Please note that this README provides a basic overview of the installation and configuration process. Refer to the official documentation for any specific requirements or troubleshooting information related to your setup.

**Disclaimer:** Make sure to consult the official Intel documentation for the most up-to-date and accurate instructions.
