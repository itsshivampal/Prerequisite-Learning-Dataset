# Prerequisite Learning Dataset
This is the dataset for learning Prerequisite Relationships using the rich information available in Textbook

## Summary
The dataset is built upon the AL-CPL dataset by Liang et al, (2018) and Wiki concept map dataset by Wang et al. (2016). For each domain, the dataset consists of prerequisite pairs, wikipedia data and Textbook data. The table below summarizes the statistics of the our final processed dataset.

Domain | # Concepts | # Pairs | # Prerequisites | # Wiki Aritcles | Concept Synonyms | Book Data
 ---   | --- | --- | --- | --- | --- | ---
 Geometry | 89 | 1681 | 524 | 89 | Available | Available
 Physics | 152 | 1962 | 487 | 152 | Available | Available
 Precalculus | 224 | 2060 | 699 | 224 | Available | Not Available 

### Textbooks
**Geometry**: [Dan Greenberg, Lori Jordan, Andrew Gloag, Victor Ci- farelli, Jim Sconyers,Bill Zahnerm, ”CK-12 Basic Geometry](https://zirklelanguagearts.files.wordpress.com/2013/01/ck-12-geometry-concepts_b_v2_0je_s1.pdf)
<br>
<br>
**Physics**: [Mark Horner, Samuel Halliday, Sarah Blyth, Rory Adams, Spencer Wheaton, ”Textbooks for High School Students Studying the Sciences”, 2008](http://nongnu.askapache.com/fhsst/fhsstadmin126-incsub.pdf )
<br>
<!-- <br> -->
<!-- **Precalculus**: [Stewart, James, Lothar Redlin, and Saleem Watson. Precalculus: Mathematics for calculus. Cengage Learning, 2015](https://erhsnyc.enschool.org/ourpages/auto/2018/9/4/44663551/Precalculus%20Book.pdf) -->

### Preprocessing of Available Dataset
Using the labelled pairs, .wikifis data and PDF Textbook of each domain, we further added Wikipedia Data (May, 2020 Dump), Concept Synoym Terms and Normalised Textbook data having ToC Section, Title and Chapter Content

## Data Description

### Raw Data

### Processed Data
- <Domain>/processed_data/<Domain>labeled_pairs.csv : Containg labeled pairs (A, B, r), if r = 1 then B is a prerequisite of A and if r = 0 then B is not a prerequisite of A
- <Domain>/processed_data/<Domain>correct_wikipedia_data.csv : Contains Wikipedia Data for each key-concepts, having - title, summary, content, html content, link structure, internal ToC of page
- <Domain>/processed_data/<Domain>normalized_content.csv : Contains normalised Textbook Data from above mentioned book, having - ToC Section, Title, Chapter Content, Normalised Chapter Content
- <Domain>/processed_data/<Domain>concepts_ambiguity.csv : Contain synonym terms for each key-concepts which can be used in place of actual concept


## Source Code
*src* folder contains all the codes which we developed for processing the data from *raw_data* to *processed_data*
- get_labeled_pairs/ : contain codes for processing labeled pairs
- get_wiki_data/ : contain codes for extracting and saving wikipedia data for concepts
- get_book_data/ : contain codes for extracting and normalizing book data
- get_concepts/ : contain codes for processing concept_ambiguity file

## Citation
```
Here we will mention the citation of our paper
```

### Refrences
Please cite the following paper if you use this data.
```
@article{liang2018investigating,
  title={Investigating Active Learning for Concept Prerequisite Learning},
  author={Liang, Chen and Ye, Jianbo and Wang, Shuting and Pursel, Bart and Giles, C Lee},
  journal={Proc. EAAI},
  year={2018}
}

@article{liang2018active,
  title={Active Learning of Strict Partial Orders: A Case Study on Concept Prerequisite Relations},
  author={Liang, Chen and Ye, Jianbo and Zhao, Han and Pursel, Bart and Giles, C Lee},
  journal={arXiv preprint arXiv:1801.06481},
  year={2018}
}

@inproceedings{wang2016using,
  title={Using prerequisites to extract concept maps fromtextbooks},
  author={Wang, Shuting and Ororbia, Alexander and Wu, Zhaohui and Williams, Kyle and Liang, Chen and Pursel, Bart and Giles, C Lee},
  booktitle={Proceedings of the 25th acm international on conference on information and knowledge management},
  pages={317--326},
  year={2016},
  organization={ACM}
}

@inproceedings{wang2015concept,
  title={Concept hierarchy extraction from textbooks},
  author={Wang, Shuting and Liang, Chen and Wu, Zhaohui and Williams, Kyle and Pursel, Bart and Brautigam, Benjamin and Saul, Sherwyn and Williams, Hannah and Bowen, Kyle and Giles, C Lee},
  booktitle={Proceedings of the 2015 ACM Symposium on Document Engineering},
  pages={147--156},
  year={2015},
  organization={ACM}
}
```
If you have any problems, please feel free to contact Shivam Pal at shivam.pal128@gmail.com