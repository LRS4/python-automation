# PDF Generator

Generates many PDFs given a docx template and csv data.

### Resources

  * [Tutorial](https://www.youtube.com/watch?v=Zh7L9GmHihQ)
  * [Conditional formatting](https://www.youtube.com/watch?v=M805tTbjsjo)
  * [Mail Merge Tips](https://www.msofficeforums.com/mail-merge/21803-mailmerge-tips-tricks.html)
  * [Raising and Lowering text](https://officemastery.com/raised-text-and-lowered-text-in-microsoft-word/)

### Excel formula

```
="Your investments have "&IF(C3<0,"fallen by ","grown by ")&"£"&TEXT(ABS(C3),"0")
```