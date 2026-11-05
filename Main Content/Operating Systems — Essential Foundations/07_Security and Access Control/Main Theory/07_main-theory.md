## Chapter 7: Security: Who May Do What

**Definition.** OS security protects the confidentiality, integrity and availability of data and resources (the CIA triad) against mistakes and attacks, by controlling who can do what and by isolating programs from each other.

**Analogy.** A building with ID badges at the door (authentication), a list of which rooms each badge opens (authorisation), and solid walls between rooms (isolation).

### 7.1 Authentication and authorisation

- **Authentication** proves who the user is: passwords (stored as salted hashes, never as plain text), multi-factor authentication, biometrics, hardware keys.

- **Authorisation** decides what that user may do. Discretionary access control (DAC) lets owners set permissions, as in Unix file modes. Mandatory access control (MAC), such as SELinux, enforces a system-wide policy that even the owner cannot override.

- **Least privilege** means every program and user gets only the rights needed for the task.

The difference between authentication and authorisation is that authentication proves who you are, while authorisation decides what you may do. Passwords should never be stored as plain text; they should be stored as salted hashes.

### 7.2 Hardware-backed protection

| **Mechanism**                                    | **What it does**                                                                           |
|--------------------------------------------------|--------------------------------------------------------------------------------------------|
| Privilege rings (kernel vs user mode)            | Stops user code from running privileged instructions                                       |
| Separate address spaces                          | Each process sees only its own virtual memory, enforced by the MMU                         |
| Page permission bits and the NX (no-execute) bit | Mark memory as read-only or non-executable so data cannot run as code                      |
| ASLR (address space layout randomisation)        | Randomises where code, stack and heap are placed, making attacks harder to aim             |
| Stack canaries and SMEP/SMAP                     | Detect stack corruption and stop the kernel from running or reading user memory by mistake |
| Virtualisation extensions (Intel VT-x, AMD-V)    | Let a hypervisor run isolated virtual machines efficiently                                 |

The NX bit stops injected data from being run as code; ASLR makes the addresses an attacker needs unpredictable. Together they make memory attacks harder.

### 7.3 Isolation above the process

Containers use kernel features (namespaces for what a process can see, cgroups for how much it can use) to isolate applications without a full virtual machine. Virtual machines isolate whole operating systems under a hypervisor.

### 7.4 Encryption and the chain of trust

- **Disk encryption** (BitLocker, LUKS, FileVault) protects data if a device is lost.

- A **TPM** (trusted platform module) chip stores keys and measures the boot chain.

- **Secure Boot** extends trust from firmware to bootloader to kernel by checking signatures at each step.

- **TLS** protects data in transit across networks.

The CIA triad stands for confidentiality, integrity and availability.

## Visual References

![Figure 7.1: File permissions with security tab](https://www.top-password.com/blog/wp-content/uploads/2017/09/security-tab-in-folder-properties.png)

*Figure 7.1. File permmissions with security tab. Source: [Top password](https://www.top-password.com/blog/wp-content/uploads/2017/09/security-tab-in-folder-properties.png).*

![Figure 7.2: Diagram of authentication vs authorisation](https://marvel-b1-cdn.bc0a.com/f00000000310757/www.fortinet.com/content/dam/fortinet/images/cyberglossary/authentication-vs-authorization-one-.jpg)

*Figure 7.2. Diagram of authentication vs authorisation. Source: [Fortinet](https://marvel-b1-cdn.bc0a.com/f00000000310757/www.fortinet.com/content/dam/fortinet/images/cyberglossary/authentication-vs-authorization-one-.jpg).*

![Figure 7.3: Overview of Secure boot](https://www.microcontrollertips.com/wp-content/uploads/2024/11/What-are-the-elements-of-secure-boot-processes-Figure-1.jpg)

*Figure 7.3. Overview of secure boot. Source: [Microcontroller tips](https://www.microcontrollertips.com/wp-content/uploads/2024/11/What-are-the-elements-of-secure-boot-processes-Figure-1.jpg).*

![Figure 7.4: Disk Encryption Settings](https://www.niallbrady.com/wp-content/uploads/2020/02/apply-operating-system-1.png)

*Figure 7.4. Disk Encryption Settings. Source: [Niall Brady](https://www.niallbrady.com/wp-content/uploads/2020/02/apply-operating-system-1.png).*

