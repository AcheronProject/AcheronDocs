# A single-push reset circuit for STM32, part 2: a more generalized approach

*Prepare for trouble. And make it double!*

**By Gondolindrim with collaborator tzarc**

**First version** published september 10, 2021

---

## 1 Introduction

In the [last article](../reset_article_1/reset_article_1.md), we discussed about the problem of selecting the boot space in STM microcontrollers, and a single-push reset circuit was developed to make the end-user more comfortable operating their devices.

Unfortunately, however, as desperating as this may seem, that was just the tip of the iceberg. In reality, other STM microcontrollers have a myriad of other boot options which, at first, can really complicate the reset circuitry needed for a low-interaction operation.

This part 2 of the *A single-push reset circuit for STM32* develops over part 1, porting the same "improved reset" circuit to other STM32 families, some times with almost no modifications at all!
