# Project Information and Write Up

## Background

The idea for this came from a discussion during an advanced movement training class with Coach Kita Busse with 180 Firearms Training. The class ended up being more of a how-to train yourself by setting goals and tracking progress on attaining those goals. To improve this requires deliberate practice and following specific goals that should be followed and recorded to track and view progress. 

## Program Setup and Information

### Athlete
For this project, the information on the athlete that will be stored in the database is the shooter’s name, current classification, and current division. These are just what is currently being trained in. A shooter in the United States Practical Shooting Association, USPSA, can hold a classification in any division at one time, as most do. The current breakdown of the USPSA divisions includes:

1. Open (Open)
2. Limited (Lim)
3. Production (Prod)
4. Single Stack (SS)
5. Revolver (Rev)
6. Carry Optics (CO)
7. Pistol Caliber Carbine (PCC)

The shortened nomenclature will be used for storing the information in the database; Production will be Prod, Carry Optics will be CO, etc. 

The classifications are broken down into Grand Master, Master, A, B, C, D, Novice, and Unclassified. To determine the shooter’s classification they are placed into a percentage bracket. The shooter’s "percentage is based on your scores as they relate to the average high scores on file for a particular course of fire. To receive an initial classification, a member needs to have at least four unduplicated scores in the USPSA classification database. If there are more than four scores on file, the best four scores of the most recent six scores will be used. Scores are sorted according to the match date to determine which scores are the most recent. For matches that are Level I Specials, the scores are further sorted by the score percent in descending order. In doing so, the lowest scores from a special will be the first scores to drop out of the most recent scores on file. After a member has earned a classification, the classification system will look at the best six unduplicated scores of the most recent eight to evaluate the member’s current classification percentage." Standard identifiers will be used in the database, please see the table below. 

| Classification | Short Id |                          Percentage |
| :------------- | :------: | ----------------------------------: |
| Grand Master   |    GM    |                           95 - 100% |
| Master         |    M     |                          85 - 94.9% |
| A Class        |    A     |                          75 - 84.9% |
| B Class        |    B     |                          60 - 74.9% |
| C Class        |    C     |                          40 - 59.9% |
| D Class        |    D     |                           Below 40% |
| Unclassified   |    U     | Not enough classifiers to calculate |

### Goals

### Steps