import streamlit as st
import google.generativeai as genai

# ==========================================
# 🟢 TEACHER: PASTE YOUR 100 PAGES BELOW
# ==========================================
PERMANENT_SYLLABUS = """
CAMBRIDGE AS LEVEL BUSINESS (9609) - SYLLABUS SUMMARY

CAMBRIDGE AS/A LEVEL BUSINESS (9609) - SYLLABUS

Key concepts
Key concepts are essential ideas that help students develop a deep understanding of their subject and make links between different aspects. Key concepts may open up new ways of thinking about, understanding or interpreting the important things to be learned.

Good teaching and learning will incorporate and reinforce a subject’s key concepts to help students gain:
a greater depth as well as breadth of subject knowledge
confidence, especially in applying knowledge and skills in new situations
the vocabulary to discuss their subject conceptually and show how different aspects link together
a level of mastery of their subject to help them enter higher education.

The key concepts identified below, carefully introduced and developed, will help to underpin the course you will teach. You may identify additional key concepts which will also enrich teaching and learning.

The key concepts for Cambridge International AS & A Level Business are:
Change
Change is the only constant. New enterprises and opportunities are created in response to change in the external environment. Change can also happen within a business, leading to success when change is handled correctly.
Context
Context is the basis for every business decision. What might be a suitable solution in one situation may be unsuitable in another. Businesses must understand and research their context to be able to make good decisions.
Decision-making
Decision-making affects all levels in a business. Stakeholders in businesses use their knowledge, apply it to a scenario, analyse the data, evaluate the arguments and then come to a decision.
Enterprise
Enterprise is the ability to seek out and successfully develop business opportunities.
Innovation
Innovation enables a business to re-invent itself and stay ahead of the competition. The business world is dynamic and companies must seek to innovate through product development, more efficient processes and finding better ways to do business.
Strategy
Strategy is about knowing where you are, where you want to get to and how you are going to get there. Being able to analyse a business situation, make choices given relevant data and then implement this effectively is key to running a successful business.




International recognition and acceptance
Our expertise in curriculum, teaching and learning, and assessment is the basis for the recognition of our programmes and qualifications around the world. Every year thousands of students with Cambridge
International AS & A Levels gain places at leading universities worldwide. Our programmes and qualifications are valued by top universities around the world including those in the UK, US (including Ivy League universities), Europe, Australia, Canada and New Zealand.

UK ENIC, the national agency in the UK for the recognition and comparison of international qualifications and skills, has carried out an independent benchmarking study of Cambridge International AS & A Level and found it to be comparable to the standard of AS & A Level in the UK. This means students can be confident that their Cambridge International AS & A Level qualifications are accepted as equivalent, grade for grade, to UK AS & A Levels by leading universities worldwide.

Cambridge International AS Level Business makes up the first half of the Cambridge International A Level course in business and provides a foundation for the study of business at Cambridge International A Level. The AS Level can also be delivered as a standalone qualification. Depending on local university entrance requirements, students may be able to use it to progress directly to university courses in business or some other subjects. It is also suitable as part of a course of general education.

Cambridge International A Level Business provides a foundation for the study of business or related courses in higher education. Equally it is suitable as part of a course of general education.

For more information about the relationship between the Cambridge International AS Level and Cambridge International A Level see the ‘Assessment overview’ section of the Syllabus overview.

We recommend learners check the Cambridge recognition database and university websites to find the most up-to-date entry requirements for courses they wish to study.

Learn more at www.cambridgeinternational.org/recognition




Supporting teachers
We believe education is most effective when curriculum, teaching and learning, and assessment are closely aligned. We provide a wide range of resources, detailed guidance, innovative training and targeted professional development so that you can give your students the best possible preparation for Cambridge International
AS & A Level. To find out which resources are available for each syllabus go to
www.cambridgeinternational.org/support

The School Support Hub is our secure online site for Cambridge teachers where you can find the resources you need to deliver our programmes. You can also keep up to date with your subject and the global Cambridge community through our online discussion forums.

Find out more at www.cambridgeinternational.org/support

Support for Cambridge International AS & A Level
Planning and preparation
Syllabuses
Schemes of work
Specimen Question Papers and Mark Schemes
Teacher guides	Teaching and assessment
Endorsed resources
Online forums	Learning and revision
Example candidate responses
Past papers and mark schemes
Specimen paper answers	Results
Candidate Results Service
Principal examiner reports for teachers

Sign up for email notifications about changes to syllabuses, including new and revised products and services, at www.cambridgeinternational.org/syllabusupdates

Syllabuses and specimen materials represent the final authority on the content and structure of all of our assessments.

Professional development
Find the next step on your professional development journey.
Introductory Professional Development – An introduction to Cambridge programmes and qualifications.
Extension Professional Development – Develop your understanding of Cambridge programmes and qualifications to build confidence in your delivery.
Enrichment Professional Development – Transform your approach to teaching with our Enrichment workshops.
Cambridge Professional Development Qualifications (PDQs) – Practice-based programmes that transform professional learning for practising teachers. Available at Certificate and Diploma level.

Find out more at:
www.cambridgeinternational.org/support-and-training-for-schools/professional-development/







2Syllabus overview


Aims
The aims describe the purposes of a course based on this syllabus.

The aims are to enable students to:
understand and appreciate the role of enterprise and the contribution of business to society – locally, nationally and internationally
develop critical understanding of business organisations, the markets they serve and the process of adding value
evaluate business behaviour from the perspective of a range of stakeholders and consider their relative influence on business organisations
develop an awareness of the political, economic, social, technological, legal, environmental and ethical issues that influence or may be influenced by business activity
apply quantitative, problem-solving, decision-making and communication skills
develop skills and knowledge needed for further study or employment in business.
































Content overview
Candidates for Cambridge International AS Level study the AS Level topics for Paper 1 and Paper 2. Candidates for Cambridge International A Level study all topics.
	AS Level topics	A Level topics
Business and its environment	1.1Enterprise
1.2Business structure
1.3Size of business
1.4Business objectives
1.5Stakeholders in a business	6.1External influences on business activity
6.2Business strategy
Human resource management	2.1Human resource management
2.2Motivation
2.3Management	7.1Organisational structure
7.2Business communication
7.3Leadership
7.4Human resource management strategy
Marketing	3.1The nature of marketing
3.2Market research
3.3The marketing mix	8.1Marketing analysis
8.2Marketing strategy
Operations management	4.1The nature of operations
4.2Inventory management
4.3Capacity utilisation and outsourcing	9.1Location and scale
9.2Quality management
9.3Operations strategy
Finance and accounting	5.1Business finance
5.2Sources of finance
5.3Forecasting and managing cash flows
5.4Costs
5.5Budgets	10.1Financial statements
10.2Analysis of published accounts
10.3Investment appraisal
10.4Finance and accounting strategy










School feedback: ‘Cambridge International AS & A Levels prepare students well for university because they’ve learnt to go into a subject in considerable depth. There’s that ability to really understand the depth and richness and the detail of a subject. It’s a wonderful preparation for what they are going to face at university.’
Feedback from: US Higher Education Advisory Council




Assessment overview

Paper 1		Paper 3
Business Concepts 1	1 hour 15 minutes
40 marks
Section A: four short answer questions. There are two parts to the first three questions.
Section B: one essay from a choice of two. There are two parts to each essay.
Questions are based on the AS Level subject content.
Externally assessed 40% of the AS Level 20% of the A Level		Business Decision-Making	1 hour 45 minutes
60 marks
Five questions based on a case study. There are three parts to Question 3 and two parts to Question 4.
Questions are based on the A Level subject content; knowledge of material from the AS Level subject content is assumed.
Externally assessed 30% of the A Level
		
Paper 2		Paper 4
Business Concepts 2	1 hour 30 minutes
60 marks
Two data response questions. There are six parts to each question.
Questions are based on the AS Level subject content.
Externally assessed 60% of the AS Level 30% of the A Level		Business Strategy	1 hour 15 minutes
40 marks
Two essay questions based on a case study.
Questions are based on the A Level subject content; knowledge of material from the AS Level subject content is assumed.
Externally assessed 20% of the A Level
Information on availability is in the Before you start section.

There are three routes for Cambridge International AS & A Level Business:

	Route	Paper 1	Paper 2	Paper 3	Paper 4
1	AS Level only
(Candidates take all AS components in the same exam series)	
yes	
yes	
no	
no
2	A Level (staged over two years) Year 1 AS Level*	
yes	
yes	
no	
no
	Year 2 Complete the A Level	no	no	yes	yes
3	A Level
(Candidates take all components in the same exam series)	
yes	
yes	
yes	
yes
* Candidates carry forward their AS Level result subject to the rules and time limits described in the Cambridge Handbook. See Making entries for more information on carry forward of results [and marks].

Candidates following an AS Level route are eligible for grades a–e. Candidates following an A Level route are eligible for grades A*–E.




Assessment objectives
The assessment objectives (AOs) are:

AO1 Knowledge and understanding
Demonstrate knowledge and understanding of business concepts, terms and theories.

AO2 Application
Apply knowledge and understanding of business concepts, terms and theories to problems and issues in a variety of familiar and unfamiliar business situations and contexts.

AO3 Analysis
Analyse business problems, issues and situations by:
using appropriate methods and techniques to make sense of qualitative and quantitative business information
searching for causes, impacts and consequences
distinguishing between factual evidence and opinion or value judgement
drawing valid inferences and making valid generalisations.

AO4 Evaluation
Evaluate evidence in order to make reasoned judgements, present substantiated conclusions and, where appropriate, make recommendations for action and implementation.




Weighting for assessment objectives
The approximate weightings allocated to each of the assessment objectives (AOs) are summarised below.

Assessment objectives as a percentage of each qualification

Assessment objective	Weighting in AS Level %	Weighting in A Level %
AO1 Knowledge and understanding	30	25
AO2 Application	30	25
AO3 Analysis	20	25
AO4 Evaluation	20	25
Total	100	100

Assessment objectives as a percentage of each component

Assessment objective		Weighting in components %	
	Paper 1	Paper 2	Paper 3	Paper 4
AO1 Knowledge and understanding	35	30	20	15
AO2 Application	30	30	27	10
AO3 Analysis	20	20	23	40
AO4 Evaluation	15	20	30	35
Total	100	100	100	100






3Subject content


This syllabus gives you the flexibility to design a course that will interest, challenge and engage your learners. Where appropriate you are responsible for selecting resources and examples to support your learners’ study. These should be appropriate for the learners’ age, cultural background and learning context as well as complying with your school policies and local legal requirements.

Cambridge International AS Level students study topics 1.1–5.5. Cambridge International A Level students study topics 1.1–10.4.
The AS Level content is assumed knowledge for A Level Paper 3 and Paper 4.


AS Level content

1	Business and its environment (AS Level)
The foundation of Business is to understand what happens within a business. At AS Level candidates develop an understanding of what a business is, what it wants to achieve and who is involved. Candidates develop the vocabulary to understand how a business operates and learn how to analyse what the business does. Every business is different, understanding its context is important to be able to understand the decisions that it makes and the motivations of those involved.
1.1Enterprise
1.1.1The nature of business activity
the purpose of business activity
the factors of production needed for business activity: land, labour, capital and enterprise
the concept of adding value
the nature of economic activity, the problem of choice and opportunity cost
the dynamic business environment
why businesses succeed or fail
differences between local, national, international and multinational businesses

1.1.2The role of entrepreneurs and intrapreneurs
the qualities entrepreneurs and intrapreneurs need for success
the role of entrepreneurship in creating and starting up a business
the role of intrapreneurship in the ongoing success of a business
barriers to entrepreneurship
business risk and uncertainty
the role of business enterprise in the development of a country






1.1	Enterprise continued
1.1.3Business plans
the meaning and purpose of business plans
the key elements of business plans
the benefits and limitations of business plans
1.2	Business structure
1.2.1Economic sectors
the primary, secondary, tertiary and quaternary sectors and businesses within those sectors
the public and private sectors and businesses within those sectors
the reasons for and consequences of the changing relative importance of these sectors

1.2.2Business ownership
the main features of different types of business ownership: sole traders, partnerships, private limited companies, public limited companies, franchises, co-operatives, joint ventures and social enterprises
the appropriateness of different types of business ownership
the concepts of unlimited liability and limited liability and their importance
the advantages and disadvantages of changing from one type of business ownership to another
1.3	Size of business
1.3.1Measurements of business size
the appropriateness of different methods of measuring the size of a business

1.3.2Significance of small businesses
the advantages and disadvantages of being a small business
the strengths and weaknesses of family businesses
the importance of small businesses and their role in the economy
the role of small businesses as part of the industrial structure in some industries

1.3.3Business growth
why and how a business might grow internally (organic growth)
the different types of external growth through merger and takeover: horizontal, vertical (backward and forward), conglomerate diversification, friendly merger, hostile takeover
the impact of a merger/takeover on stakeholders
why a merger/takeover may or may not achieve objectives
the importance of joint ventures and strategic alliances as methods of external growth






1.4	Business objectives
1.4.1Business objectives in the private sector and public sector
the objectives of businesses – private sector, public sector, and social enterprises
the importance of business objectives
corporate social responsibility (CSR) and the triple bottom line – economic (financial), social and environmental objectives
the relationship between mission statement, aims, objectives, strategy and tactics

1.4.2Objectives and business decisions
the different stages of business decision-making and the role of objectives in the stages of business decision-making
how objectives might change over time
the translation of objectives into targets and budgets
the need for communication of objectives and their likely impact on the workforce
SMART (specific, measurable, achievable, realistic, time-limited) objectives
how ethics may influence business objectives and activities
1.5	Stakeholders in a business
1.5.1Business stakeholders
individuals or groups with an interest in the activities of a business
internal stakeholders and external stakeholders
the roles, rights and responsibilities of stakeholders

1.5.2The relative importance and infuence of stakeholders on business activities
the impact of business decisions on stakeholders, and their reactions
the impact of stakeholder aims on business decisions
how and why a business needs to be accountable to its stakeholders
how conflict might arise from stakeholders having different aims and objectives
how changing business objectives might affect its stakeholders






2	Human resource management (AS Level)
The focus of this topic is on how a business can effectively manage its workforce to achieve its objectives. Candidates will develop an understanding of the human resource management process from planning and recruiting workers through to their dismissal. Candidates will learn about motivation in management. They will learn about the theory behind motivation as well as how to implement it in practice.
2.1Human resource management (HRM)
2.1.1Purpose and roles of HRM
the role of HRM in meeting organisational objectives

2.1.2Workforce planning
the reasons for and role of a workforce plan
measurement of labour turnover
the implications of high and low labour turnover for a business

2.1.3Recruitment and selection
recruitment of employees: process (job descriptions and person specifications) and recruitment methods (job advertisements, employment agencies, online recruitment)
internal and external recruitment
selection methods: curriculum vitae, résumé, application forms, interviews, references, testing, assessment centres
employment contracts

2.1.4Redundancy and dismissal
the difference between redundancy (voluntary and involuntary) and dismissal (fair, unfair)

2.1.5Morale and welfare
the relationship between HRM, employee morale and welfare in a business including the concept of work-life balance
the impact of diversity and equality in the workplace on a business

2.1.6Training and development
different types of training: induction, on-the-job, off-the-job
the impact of training and development on a business
employee development to encourage intrapreneurship
employee development to encourage multi-skilling and flexibility






2.1	Human resource management (HRM) continued
2.1.7Management and workforce relations
how cooperation between management and the workforce can be of benefit to both
the impact on employers and employees of trade union involvement in the workplace including their role in collective bargaining
2.2	Motivation
2.2.1Motivation as a tool of management and leadership
the need to motivate employees to achieve the objectives of a business

2.2.2Human needs
a simple explanation of human need
how human needs may or may not be satisfied at work

2.2.3Motivation theories
the ideas of the main content theories (Taylor, Mayo, Maslow, Herzberg and McClelland) and process theory (Vroom)


2.2.4Motivation methods in practice: financial motivators, non-financial motivators
the theories in practical situations
different payment methods: time based, salary, piece rates, commission, bonuses, profit sharing, performance-related pay, fringe benefits
different types of non-financial motivators: training, opportunities for promotion, development, status, job re-design, team working, empowerment, participation, job enrichment
ways in which employees can participate in the management and control of business activity
2.3	Management
2.3.1Management and managers
traditional manager functions: planning, organising, directing, controlling
the role of managers: Fayol, Mintzberg
the contribution of managers to business performance
management styles: autocratic, democratic, laissez-faire, paternalistic
McGregor’s Theory X and Theory Y managers






3	Marketing (AS Level)
The focus of this topic is on how a business finds out the needs of potential customers, and provides for their needs. Candidates will develop an understanding of the marketing mix. Candidates will have the
opportunity to study in further depth one or more of the elements of the marketing mix, and to develop the skills to be able to recommend a suitable marketing mix for a business in a specific context.
3.1The nature of marketing
3.1.1The role of marketing and its relationship with other business activities
marketing objectives
the link between marketing objectives and corporate objectives

3.1.2Demand and supply
the factors influencing the demand for and supply of the products of a business
interactions between demand, supply and price

3.1.3Markets
how markets may differ: consumer and industrial markets; local, national and international markets
the difference between product orientation and customer (market) orientation
measurement of market share and market growth
the implications of changes in market share and market growth

3.1.4Consumer and industrial marketing
the classification of products
how marketing might differ for consumer products (B2C – business to consumer) and industrial products (B2B – business to business)


3.1.5Mass marketing and niche marketing
the features of mass and niche markets
the advantages and disadvantages of mass marketing and niche marketing

3.1.6Market segmentation
methods of market segmentation: geographic, demographic and psychographic
the advantages and disadvantages of market segmentation

3.1.7Customer relationship marketing (CRM)
the aims of CRM
the costs and benefits of CRM






3.2	Market research
3.2.1The purposes of market research
identification of main features of a market: size, growth, competitors
identification of customer and consumer characteristics, profiles, wants and needs

3.2.2Primary research and secondary research
the distinction between primary research and secondary research, and the main features of each
usefulness of data collected using primary research methods
usefulness of data collected from secondary research sources

3.2.3Sampling
the need for and limitations of sampling

3.2.4Market research data
the reliability of the data collected
analysis of quantitative and qualitative data
interpretation of information presented in tables, charts and graphs
3.3	The marketing mix
3.3.1The elements of the marketing mix (the 4Ps)
the 4Ps: Product, Price, Promotion, Place (distribution channels)

3.3.2Product
the difference between goods and services
tangible and intangible attributes of products
the importance of product development
product differentiation and unique selling point (USP)

3.3.3Product portfolio analysis
product life cycle and decisions about extension strategies
Boston Matrix analysis and its uses
impact of product portfolio analysis on marketing decisions






3.3	The marketing mix continued
3.3.4Pricing methods
objectives and usefulness of different pricing methods: competitive, penetration, skimming, price discrimination, dynamic, cost-based and psychological


3.3.5Promotion methods
the objectives and usefulness of different promotion methods
advertising promotion
sales promotion
direct promotion
developments in digital promotion
the role of packaging in promotion
the role of branding in promotion

3.3.6Place (channels of distribution)
the objectives and usefulness of different channels of distribution
digital and physical distribution

4	Operations management (AS Level)
The focus of this topic is on operations management from the production of physical products to managing the process of creating services. There are different ways a business can produce a product, with a
range of aspects to consider in its production. Candidates are provided with the opportunity to apply their understanding of production methods in a variety of business contexts.
4.1The nature of operations
4.1.1The transformational process
the use of factors of production: land, labour, capital and enterprise
the stages of the transformational process: inputs to outputs
the contribution of operations to added value

4.1.2Efficiency, effectiveness, productivity and sustainability
the importance of efficiency, effectiveness, productivity and sustainability
measurement of labour productivity
the impact on a business of measures to improve sustainability of operations






4.1	The nature of operations continued
4.1.3Capital intensive and labour intensive operations
the benefits and limitations of capital intensive operations
the benefits and limitations of labour intensive operations

4.1.4Operations methods: job, batch, flow, mass customisation
differences between methods – advantages and disadvantages of each method
the problems of changing from one method to another
4.2	Inventory management
4.2.1Managing inventory
the purpose of inventory within a business (raw materials, work in progress, finished products)
the costs and benefits of holding inventory
buffer inventory, re-order level and lead time
interpretation of simple inventory control charts
the importance of Supply Chain Management

4.2.2Just in Time (JIT)
the purpose of JIT and JIC (Just in Case) inventory management
the impact of adopting a JIT approach on a business
4.3	Capacity utilisation and outsourcing
4.3.1Significance and measurement of capacity utilisation
the measurement of capacity utilisation
the impact of operating under or over maximum capacity on a business
methods of improving capacity utilisation

4.3.2Outsourcing
the impact of outsourcing on a business






5	Finance and accounting (AS Level)
The focus of this topic is on the areas more traditionally associated with finance such as how a business can fund itself and where that money goes. Candidates will learn why a business requires finance to operate, and the importance for businesses to successfully manage their finance.
5.1Business finance
5.1.1The need for business finance
reasons why businesses need finance to start up, to grow and to survive
the distinction between short and long term need for finance
the difference between cash and profits
business failure as a consequence of lack of finance: bankruptcy, liquidation and administration

5.1.2Working capital
the meaning and importance of working capital
managing trade receivables and trade payables
the distinction between capital expenditure and revenue expenditure
5.2	Sources of finance
5.2.1Business ownership and sources of finance
the relationship between the form of business ownership and availability of sources of finance

5.2.2Internal and external sources of finance
internal sources of finance: owners investment, retained earnings, sale of unwanted assets, sale and leaseback of non-current assets, working capital
external sources of finance: share capital, debentures, new partners, venture capital, bank overdrafts, leasing, hire purchase, bank loans, mortgages, debt factoring, trade credit, micro-finance, crowd funding and government grants


5.2.3Factors affecting the sources of finance
the factors influencing the choice of sources of finance in a given situation: cost, flexibility, need to retain control, the use to which it is put, level of existing debt


5.2.4Selecting the source of finance
the appropriateness of each possible source in a given situation






5.3	Forecasting and managing cash flows
5.3.1Cash flow forecasts
the meaning and purpose of cash flow forecasts
the interpretation and amendment of simple cash flow forecasts: calculating opening and closing balances
different methods of improving cash flow
5.4	Costs
5.4.1Cost information
the need for accurate cost information
different types of costs: fixed, variable, direct and indirect

5.4.2Approaches to costing: full, contribution
the differences between full and contribution costing
the uses and limitations of the full costing method
the nature of the technique of contribution costing
the difference between contribution and profit
the limitations of contribution costing
situations in which contribution costing would be and would not be used

5.4.3Uses of cost information
cost information for decision-making purposes, e.g. average, marginal, total costs
how costs can be used for pricing decisions
how costs can be used to monitor and improve business performance, including using cost information to calculate profits
contribution costing as a means to help make special order decisions

5.4.4Break-even analysis
the meaning and importance of break-even analysis
calculation and interpretation of break-even level of output, contribution, margin of safety and level of profit (in numeric and graphic form)
the uses and limitations of break-even analysis






5.5	Budgets
5.5.1The meaning and purpose of budgets
the measurement of performance
the benefits and drawbacks from the use of budgets
the meaning and use of incremental budgets, flexible budgets and zero budgeting
the uses of budgets for measuring performance, allocating resources, controlling and monitoring a business

5.5.2Variances
the meaning of adverse variances and favourable variances
the calculation and interpretation of variances

A Level content
The content of the AS Level is assumed knowledge for the assessment of Paper 3 and Paper 4. The A Level topics build on the learning acquired in the AS Level topics.

6	Business and its environment (A Level)
This A Level topic builds on the learning acquired in topic 1, enabling candidates to further understand the environment in which a business operates. All businesses operate in a constantly changing environment. Candidates will develop an understanding that although some aspects of the environment are fixed, businesses operate in a context in which things change. The way in which the topic is taught should reflect the changing needs of the environment in which a business operates.

The study of business strategy will enable candidates to develop their skills to produce a basic business strategy. Candidates will develop an understanding of the tools a business uses to analyse the internal and external environment to ensure the success of the business.
6.1External influences on business activity
6.1.1Political and legal
the advantages and disadvantages of privatisation in a given situation
the advantages and disadvantages of nationalisation in a given situation
how a government might use the law to seek to control: employment practices, conditions of work (including health and safety), wage levels, marketing behaviour, competition, location decisions, particular goods and services
the impact of changes in political and legal factors on business and business decisions






6.1	External influences on business activity continued
6.1.2Economic
how government might intervene to help businesses and encourage enterprise
how government might intervene to constrain business activity
how government might deal with market failure
the key macroeconomic objectives of governments: low unemployment, low inflation, economic growth
how macroeconomic objectives and performance of an economy can have an impact on business activity
government policies used to achieve macroeconomic objectives: monetary, fiscal, supply-side and exchange rate policies
the impact of changes in these government policies on business and business decisions

6.1.3Social and demographic
the impact of and issues associated with corporate social responsibility (CSR), e.g. accounting practices, paying incentives for the award of contracts, social auditing
why businesses need to consider the needs of the community including pressure groups
demographic changes at a local, national and global level
the impact of social and demographic change on business and business decisions

6.1.4Technological
the impact of technological change on business and business decisions

6.1.5Competitors and suppliers
the impact of competitors and suppliers on business and business decisions

6.1.6International
the importance of international trading links and their impact on business and business decisions
how international trade agreements might have an impact on businesses
the role of technology in international trade
the advantages and disadvantages that a multinational might bring to a country
relationships between multinationals and governments

6.1.7Environmental
how physical environmental issues might influence business behaviour
how a business and its stakeholders may use an environmental audit
the impact of the growing importance of sustainability on business and business decisions






6.2	Business strategy
6.2.1Developing business strategy
the meaning and purpose of business strategy
the meaning and purpose of strategic management: analysis, choice and implementation
approaches to develop business strategy, including:
–blue ocean strategy
–scenario planning
–SWOT analysis
–PEST analysis
–Porter’s five forces
–core competence framework
–Ansoff matrix
–force field analysis
–decision trees

6.2.2Corporate planning and implementation
the meaning and importance of corporate planning
the meaning of corporate culture and its impact on business decision-making
the meaning and importance of transformational leadership
the management and control of strategic change
the meaning and importance of contingency planning and crisis management

7	Human resource management (A Level)
This A Level topic builds on the learning acquired in topic 2, enabling candidates to build the bigger picture of managing a workforce. Candidates will develop an understanding of the different ways in which a business can structure its workforce to reach its goals. Candidates will learn about business leadership and the ability to make decisions. Candidates will develop an understanding that there are different ways to lead. The most suitable method will depend on the business, and its context.

The study of strategic elements of human resource management will require candidates to bring together the content learnt in topic 2 and in this topic 7 to think about how a business can manage its people from a business-wide perspective.
7.1Organisational structure
7.1.1The relationship between business objectives and organisational structure
the purpose and attributes of an organisational structure such as flexibility, meeting the needs of the
business, allowing for growth and development and encouraging intrapreneurship






7.1	Organisational structure continued
7.1.2Types of structure: functional, hierarchical (flat and narrow), matrix
the advantages and disadvantages of the different types of structure
why some organisations are structured by product and others by function or geographical area
the reasons and ways structures change e.g. due to growth or delayering
the features of a formal structure: levels of hierarchy, chain of command, span of control, responsibility, authority, delegation, accountability, centralised, decentralised

7.1.3Delegation and accountability
the relationship between delegation and accountability
the processes of accountability in a business
the impact of delegation on a business

7.1.4Control, authority and trust
the relationship between span of control and levels of hierarchy
the difference between authority and responsibility
the conflicts between control and trust that might arise when delegating

7.1.5Centralisation and decentralisation
the impact of centralisation and decentralisation on a business

7.1.6Line and staff
examples of and distinctions between line and staff functions and the conflicts between them
7.2	Business communication
7.2.1Purposes of communication
situations in which communication is essential

7.2.2Methods of communication
the standard methods of communication used in business: spoken, written, electronic, visual
the strengths and weaknesses of the different methods of communication






7.2	Business communication continued
7.2.3Channels of communication
how communication works within a business
the difference between one- and two-way communication; the difference between vertical and horizontal communication
problems associated with different channels of communication

7.2.4Barriers to communication
barriers to communication and how to overcome them

7.2.5The role of management in facilitating communication
the role of informal communications within a business
ways in which communication can influence the efficiency of a business
ways of improving communication in a given situation
7.3	Leadership
7.3.1Leadership
the purpose of leadership
leadership roles in business (directors, managers, supervisors, worker representatives)
the qualities of a good leader

7.3.2Theories of leadership
key leadership theories: trait, behavioural, contingency, power and influence and transformational

7.3.3Emotional intelligence/emotional quotient (EQ)
Goleman’s four competencies of emotional intelligence: self-awareness, social awareness, self- management and social skills
7.4	Human resource management (HRM) strategy
7.4.1Approaches to human resource management (HRM)
the difference between ‘hard’ and ‘soft’ HRM
flexible working contracts: advantages and disadvantages of temporary contracts or flexible contracts including zero hours contracts, part-time, full-time, annualised hours, flexi-time, home working, shift working, job sharing, compressed working hours, the gig economy
the measurement, causes and consequences of poor employee performance
strategies for improving employee performance
Management by Objectives (MBO) – implementation and usefulness
the changing role of Information Technology (IT) and Artificial Intelligence (AI) in HRM






8	Marketing (A Level)
The focus of this A Level topic is on how a business can plan and strategise for the future. Candidates will build from their learning in topic 3 to plan for the future marketing needs of the business.

The study of the strategic elements of marketing, include learning about the marketing plan which includes the whole process of marketing, not just the marketing mix. Candidates will look at how a business can adapt and change their marketing to focus on international markets.
8.1Marketing analysis
8.1.1Elasticity
the concept of elasticity of demand: price, income and promotional
calculation of price, income and promotional elasticity of demand
interpretation of elasticity results
the impact of elasticity measures on business decisions
the limitations of the concept of elasticity in its various forms

8.1.2Product development
the process of product development
sources of new ideas for product development
the importance of Research and Development (R&D)

8.1.3Sales forecasting
the need to forecast sales
time series analysis: calculation and use of four period centred moving average method to forecast sales
qualitative sales forecasting
the impact of sales forecasting on business decisions
8.2	Marketing strategy
8.2.1Planning the marketing strategy
the contents of a marketing plan: objectives, resources, research, marketing mix
the benefits and limitations of marketing planning

8.2.2Approaches to marketing strategy
the need for the marketing strategy to be consistent with the business, the product and the market
the need for and development of a coordinated marketing strategy
the development of marketing strategies that are focused towards achieving specific marketing objectives
the changing role of Information Technology (IT) and Artificial Intelligence (AI) in marketing






8.2	Marketing strategy continued
8.2.3Strategies for international marketing
the implications for marketing of increased globalisation and economic collaboration
the importance of international marketing for a business
international markets – identification, selection and entry
whether a business in a given situation should develop an international market through pan-global marketing or maintain local differences
choosing a strategy, in a given situation, to develop a global market
the factors influencing the method of entry into international markets

9	Operations management (A Level)
This A Level topic builds on the learning acquired in topic 4, enabling candidates to study the wider aspects of production. Candidates will develop an understanding of the importance of the location of a business and the effect that the location has on other aspects of the operations of the business. Candidates will learn about the importance of quality and the effect that quality has on the other functional areas of business.
Candidates will develop an awareness of quality in terms of operations management (i.e. being ‘fit for purpose’) as opposed to a customer’s perception of quality of a product.
Candidates will learn about various aspects of operations strategy, including the longer-term planning needed to improve the operations of a business, innovations such as enterprise resource planning (ERP) and lean production, and tools such as critical path analysis.
9.1Location and scale
9.1.1Location
the factors that determine location and relocation
the differences between local, national and international location decisions
the reasons for and impact of offshoring and reshoring
the impact of globalisation on location and relocation decisions

9.1.2Scale of operations
the factors that influence the scale of a business
causes and examples of internal and external economies and diseconomies of scale
the links between economies and diseconomies of scale and unit costs






9.2	Quality management
9.2.1Quality control and quality assurance
quality in terms of meeting customer expectations
the importance of quality
the impact of methods of quality control on a business
the impact of methods of quality assurance on a business
the impact of Total Quality Management (TQM) on a business

9.2.2Benchmarking
the importance of benchmarking in quality management
9.3	Operations strategy
9.3.1Operational decisions
the influence of human, marketing and finance resource availability on operations decisions
the changing role of Information Technology (IT) and Artificial Intelligence (AI) in operations management

9.3.2Flexibility and innovation
the need for flexibility with regard to volume, delivery time and specification
process innovation: changing current processes or adopting new ways of producing products or delivering services

9.3.3Enterprise resource planning (ERP)
the main features of an ERP programme
how ERP can improve a business’ efficiency in relation to: inventory control, costing and pricing, capacity utilisation, responses to change, workforce flexibility, management information

9.3.4Lean production
the aims and purposes of lean production
Kaizen, quality circles, simultaneous engineering, cell production, JIT manufacturing and waste management as operational strategies to achieve lean production
the limitations of operational strategies to achieve lean production
the links between lean production and inventory control, quality, employees roles, capacity management
and efficiency






9.3	Operations strategy continued
9.3.5Operations planning
the need for planning operations
network diagrams as tools to plan operations
the main elements of a network diagram: activities, dummy activities, nodes
network diagrams as means of performing Critical Path Analysis (CPA), including identification of the minimum project duration and the critical path, calculation of total and free float, interpretation of the results of the analysis of a network, how minimum duration and floats might be used in project management
the benefits and limitations of CPA as a management tool

10	Finance and accounting (A Level)
This A Level topic builds on the learning acquired in topic 5, with a focus on accounting information, including published accounts.

Candidates will develop an understanding of what can be learnt from the accounts of a business.

Candidates are not expected to be able to draw up a set of accounts. However, candidates do need to be able to calculate relevant ratios and use this data to inform business decisions.
10.1Financial statements
10.1.1Statement of profit or loss
the meaning and purpose of the statement of profit or loss
the contents of a statement of profit or loss: revenue, cost of sales, gross profit, expenses, profit from operations (operating profit), taxation, profit for the year, dividends, retained earnings
amendment of a statement of profit or loss
the impact on the statement of profit or loss of a given change

10.1.2 Statement of financial position
the meaning and purpose of statement of financial position
the contents of a statement of financial position including non-current assets, current assets, current liabilities, net current assets, net assets, non-current liabilities, reserves and equity
amendment of a statement of financial position
the relationships between items in the statement of profit or loss and the statement of financial position

10.1.3 Inventory valuation
the difficulties of valuing inventory
the net realisable value method






10.1	Financial statements continued
10.1.4 Depreciation
the role of depreciation in the accounts
the impact of depreciation (straight-line method only) on the statement of financial position and the statement of profit or loss
10.2	Analysis of published accounts
10.2.1Liquidity ratios
the meaning and importance of liquidity
current ratio: calculation and interpretation
acid test ratio: calculation and interpretation
methods of improving liquidity

10.2.2 Profitability ratios
the meaning and importance of profitability
return on capital employed: calculation and interpretation
gross profit margin: calculation and interpretation
profit margin: calculation and interpretation
methods of improving profitability

10.2.3 Financial efficiency ratios
the meaning and importance of financial efficiency
rate of inventory turnover: calculation and interpretation
trade receivables turnover (days): calculation and interpretation
trade payables turnover (days): calculation and interpretation
methods of improving financial efficiency

10.2.4 Gearing ratio
the meaning and importance of gearing
gearing ratio: calculation and interpretation
methods of improving gearing

10.2.5 Investment ratios
the meaning and importance of return to investors
dividend yield: calculation and interpretation
dividend cover: calculation and interpretation
price/earnings ratio: calculation and interpretation
methods of improving investor return






10.3	Investment appraisal
10.3.1The concept of investment appraisal
the need for investment appraisal

10.3.2 Basic methods: payback, accounting rate of return (ARR)
the meaning, calculation and interpretation of payback and ARR (ARR = (average profit / average investment) × 100)

10.3.3 Discounted cash flow method: net present value (NPV)
the meaning, calculation and interpretation of NPV

10.3.4 Investment appraisal decisions
quantitative results and their impact on investment decisions
qualitative factors and their impact on investment decisions
comparison of investment appraisal methods, including their limitations
10.4	Finance and accounting strategy
10.4.1The use of accounting data to enable strategic decision-making
the use of financial statements in developing strategies
the contents of an annual report and their usefulness to business and other stakeholders

10.4.2 The use of accounting data and ratio analysis in strategic decision-making
assessment of business performance over time and against competitors
the impact of accounting data including ratio results on business strategy
the impact of debt or equity decisions on ratio results
the impact of changes in dividend strategy on ratio results
the impact of business growth on ratio results
the impact of other business strategies on ratio results
the limitations of using published accounts and ratio analyses




Ratios to support analysis of published accounts
Liquidity ratios


Current ratio	 Current assets  Current liabilities
Answer presented as a ratio

Acid test ratio	Current assets – inventory Current liabilities
Answer presented as a ratio


Profitability ratios

Gross profit margin (%)	Gross profit × 100 Revenue
Operating profit margin (%)	 Profit from operations × 100 Revenue

Return on capital employed (%)	 Profit from operations  × 100 Capital employed
Capital employed = issued shares + reserves + non-current liabilities


Financial efficiency ratios

Trade receivables turnover (days)	Trade receivables × 365 days Credit sales
Trade payables turnover (days)	 Trade payables  × 365 days Credit purchases
Rate of inventory turnover (times)	 Cost of sales	 Average inventory


Gearing ratio

Gearing (%)	Non-current liabilities × 100 Capital employed




Investment ratios

Price/earnings ratio	Market price per share Earnings per share
Dividend yield (%)	 Dividend per share  × 100 Market price per share
Dividend cover	Profit for the year Annual dividend






4Details of the assessment


Paper 1 – Business Concepts 1
Written paper, 1 hour 15 minutes, 40 marks This paper contains two sections.
Section A contains four compulsory questions of five marks each.
Section B contains two questions of 20 marks; candidates answer one question. Section A has four questions. The first three questions have two parts.
Section B questions are essay questions and have two parts. Answers to the second part of the questions should show evidence of evaluation (AO4).

The questions are based on the AS Level syllabus content (topics 1.1–5.5).

Paper 1 assesses AO1 Knowledge and understanding, AO2 Application, AO3 Analysis and AO4 Evaluation.


Paper 2 – Business Concepts 2
Written paper, 1 hour 30 minutes, 60 marks

This paper contains two compulsory questions of 30 marks each.

Each question includes a text containing data, which includes information in written, numerical and/or diagrammatic form. Candidates need to answer the question using relevant and appropriate information from the stimulus text to support their answers. Each question has six parts. Answers to the last part of the questions should show evidence of evaluation (AO4).

The questions are based on the AS Level syllabus content (topics 1.1–5.5).

Paper 2 assesses AO1 Knowledge and understanding, AO2 Application, AO3 Analysis and AO4 Evaluation.




Paper 3 – Business Decision-Making
Written paper, 1 hour 45 minutes, 60 marks

This paper contains five compulsory questions. The first two questions are worth 8 marks each. Question 3 and Question 4 are worth 16 marks each. Question 5 is worth 12 marks.

The paper includes a case study, which includes information in written, numerical and/or diagrammatic form. Candidates need to answer the questions using relevant and appropriate information from the stimulus text to support their answers.

Question 1, Question 2 and Question 5 are not divided into parts. There are three parts to Question 3 and two parts to Question 4. Answers to the last part of the questions of Question 3 and Question 4 should show evidence of evaluation (AO4). Answers to Question 5 should also show evidence of evaluation (AO4).

For Paper 3, candidates will answer on the question paper. The case study will be presented separately in an insert.

The questions are based on the A Level syllabus content (topics 6.1–10.4). The content of the AS Level (topics 1.1–5.5) is assumed knowledge for the assessment of Paper 3. The AS Level content will not be the direct focus of questions on Paper 3.

Paper 3 assesses AO1 Knowledge and understanding, AO2 Application, AO3 Analysis and AO4 Evaluation.


Paper 4 – Business Strategy
Written paper, 1 hour 15 minutes, 40 marks

This paper contains two compulsory questions of 20 marks each.

The paper includes a case study, which includes information in written, numerical and/or diagrammatic form. Candidates need to answer the questions using relevant and appropriate information from the stimulus text to support their answers.

Both questions are essay questions. Answers to both questions should show evidence of evaluation (AO4).

The questions are based on the A Level syllabus content (topics 6.1–10.4). The content of the AS Level (topics 1.1–5.5) is assumed knowledge for the assessment of Paper 4. The AS Level content will not be the direct focus of questions on Paper 4.

Paper 4 assesses AO1 Knowledge and understanding, AO2 Application, AO3 Analysis and AO4 Evaluation.




Command words
Command words and their meanings help candidates know what is expected from them in the exams. The table below includes command words used in the assessment for this syllabus. The use of the command word will relate to the subject context.

Command word	What it means
Advise	write down a suggested course of action in a given situation
Analyse	examine in detail to show meaning, identify elements and the relationship between them
Assess	make an informed judgement
Calculate	work out from given facts, figures or information
Define	give precise meaning
Evaluate	judge or calculate the quality, importance, amount, or value of something
Explain	set out purposes or reasons / make the relationships between things clear / say why and/or how and support with relevant evidence
Identify	name/select/recognise
Justify	support a case with evidence/argument

Additional guidance, e.g. phrases such as ‘To what extent …?’ may also be seen in the assessment for this syllabus.


CAMBRIDGE AS/A2 LEVEL BUSINESS (9609) - DEFINISIONS


1.Globalisation or Globalization – the increasing freedom of movement of goods, capital and people around the world
2.Free trade – no restrictions or trade barriers exist that might prevent or limit trade between countries
3.Tariffs – taxes imposed on imported goods to make them more expensive than they would otherwise be
4.Quotas – limits on the physical quantity or value of certain goods that may be imported
5.Voluntary export limits – an exporting country agrees to limit the quantity of certain goods sold to one country (possibly to discourage the setting of tariffs/quotas)
6.Protectionism – using trade barriers to free trade to protect a country’s own domestic industries
7.Multinational business – business organisation that has its headquarters in one country, but with operating branches, factories and assembly plants in other countries
8.Privatisation – selling state-owned and controlled business organisations to investors in the private sector
9.External growth – business expansion achieved by means of merging with or taking over another business, from either the same or different industry
10.Merger – an agreement by shareholders and managers of two businesses to bring both firms together under a common board of directors with shareholders in both businesses owning shares in the newly merged business
11.Takeover – when a company buys more than 50% of the shares of another company and becomes the controlling owner of it – often to as ‘acquisition’
12.Synergy – literally means that ‘the whole is greater than the sum of parts’, so in integration it is often assumed that the new, larger business will be more successful than the two formerly separate, businesses were
13.Monopoly – theoretically a situation in which there is only one supplier, but this is very rare: for government policy purposes this is usually redefined as a business controlling at least 25% of the market

14.Social audit – a report on the impact a business has on society – this can cover pollution levels, health and safety record, sources of supplies, customer satisfaction and contribution to the community
15.Information technology – the use of electronic technology to gather, store, process and communicate information
16.Innovation – creating more effective processes, products or ways of doing things in a business
17.Computer-aided design (CAD) – using computers and IT when designing products
18.Computer-aided manufacturing (CAM) – the use of computers and computer-controlled machinery to speed up the production process and make it more flexible
19.Environmental audits – assess the impact of a business’s activities on the environment
20.Social audit – a report on the impact a business has on society. This can cover pollution levels, health and safety record, sources of supplies, customer satisfaction and contribution to the community
21.Pressure groups – organisations created by people with a common interest or aim who put pressure on businesses and governments to change policies so that an objective is reached
22.Economic growth – an increase in a country’s productive potential measured by an increase in its real GDP
23.Gross domestic product (GDP) – the total value of goods and services produced in a country in one year – real GDP has been adjusted for inflation.
24.Business investment – expenditure by businesses on capital equipment, new technology and research and development
25.Business cycle – the regular swings in economic activity, measured by real GDP, that occur in most economies, varying from boom conditions (high demand and rapid growth) to recession when total national output declines
26.Recession – a period of six months or more of declining real GDP
27.Inflation – an increase in the average price level of goods and services – it results in a fall in the value of money
28.Deflation – a fall in the average price level of goods and services
29.Working population – all those in the population of working age who are willing and able to work
30.Unemployment – this exists when members of the working population are willing and able to work, but are unable to find a job

31.Cyclical unemployment – unemployment resulting from low demand for goods and services in the economy during a period of slow economic growth or recession
32.Structural unemployment – unemployment caused by the decline in important industries, leading to significant job losses in one sector of industry
33.Frictional unemployment – unemployment resulting from workers losing or leaving jobs and taking a substantial period of time to find alternative employment
34.Balance of payments (current account) – this account records the value of trade in goods and services between one country and the rest of the world. A deficit means that the value of goods and services imported exceeds the value of goods and services exported
35.Exchange rate – the price of one currency in terms of another
36.Exchange rate depreciation – a fall in the external value of a currency as measured by its exchange rate against other currencies. If $1 falls in value from €2 to €1.5, the value of the dollar has depreciated in value
37.Imports – goods and services purchased from other countries
38.Exports – goods and services sold to consumers and business in other countries
39.Exchange rate appreciation – a rise in the external value of a currency as measured by its exchange rate against other currencies. If $1 rises from
€1.5 to €1.8, the value of the dollar has appreciated
40.Fiscal policy – concerned with decisions about government expenditure, tax rates and government borrowing – these operate largely through the government’s annual budget decisions
41.Government budget deficit – the value of government spending exceeds revenue from taxation
42.Government budget surplus – taxation revenue exceeds the value of government spending
43.Monetary policy – is concerned with decisions about the rate of interest and the supply of money in the economy
44.Market failure – when markets fail to achieve the most efficient allocation of resources and there is under- or overproduction of certain goods or services
45.External costs – costs of an economic activity that are not paid for by the producer or consumer, but by the rest of society
46.Income elasticity of demand – measures the responsiveness of demand for a product after a change in consumer incomes

47.Hard HRM – an approach to managing staff that focuses on cutting costs, e.g., temporary and part-time employment contracts, offering maximum flexibility but with minimum training costs
48.Soft HRM – an approach to managing staff that focuses on developing staff so that they reach self-fulfilment and are motivated to work hard and stay with the business
49.Part-time employment contract – employment contract that is for less than the normal full working week of, say, 40 hours, e.g., eight hours per week
50.Temporary employment contract – employment contract that lasts for a fixed time period, e.g., six months
51.Flexi-time contract – employment contract that allows staff to be called in at times most convenient to employers and employees, e.g., at busy times of day
52.Outsourcing – not employing staff directly, but using an outside agency or organisation to carry out some business functions
53.Teleworking – staff working from home but keeping contact with the office by means of modern IT communications
54.Zero-hours contract – no minimum hours of work are offered and workers are only called in-and paid-when work is available
55.Labour productivity – the output per worker in a given time period Labour productivity = total output in time period/total workers employed
56.Absenteeism – measures the rate of workforce absence as a proportion of the employee total
Absenteeism = no. of employees absents/total no. of employees * 100
57.Workforce planning – analysing and forecasting the numbers of workers and the skills of those workers that will be required by the organisation to achieve its objectives
58.Workforce audit – a check on the skills and qualifications of all existing workers/managers
59.Trade union – an organisation of working people with the objective of improving the pay and working conditions of their members and providing them with support and legal services
60.Trade union recognition – when an employer formally agrees to conduct negotiations on pay and working conditions with a trade union rather than bargain individually with each worker
61.Collective bargaining – the process of negotiating the terms of employment between an employer and a group of workers who are usually represented by a trade union official

62.Terms of employment – include working conditions, pay, work hours, shift length, holidays, sick leave, retirement benefits and health care benefits
63.Single-union agreement – an employer recognises just one union for purposes of collective bargaining
64.No-strike agreement – unions agree to sign a no-strike agreement with employers in exchange for greater involvement in decisions that affect the workforce
65.Industrial action – measures taken by the workforce or trade union to put pressure on management to settle an industrial dispute in favour of employees
66.Organisational structure – the internal, formal framework of a business that shows the way in which management is organised and linked together and how authority is passed through the organisation
67.Matrix structure – an organisational structure that creates project teams that cut across traditional functional departments
68.Level of hierarchy – a stage of the organisational structure at which the personnel on it have equal status and authority
69.Chain of command – this is the route through which authority is passed down an organisation – from the chief executive and the board of directors
70.Span of control – the number of subordinates reporting directly to a manager
71.Delegation – passing authority down the organisational hierarchy
72.Centralisation: keeping all of the important decision-making powers within head office or the centre of the organisation
73.Decentralisation: decision-making powers are passed down the organisation to empower subordinates and regional/product managers
74.Delayering – removal of one or more of the levels of hierarchy from an organisational structure
75.Line managers – managers who have direct authority over people, decisions and resources within the hierarchy of an organisation
76.Staff managers – managers who, as specialists, provide support, information and assistance to line managers
77.Informal organisation – the network of personal and social relations that develop between people within an organisation
78.Effective communication – the exchange of information between people or groups, with feedback
79.Communication media – the methods used to communicate a message

80.Information overload: so much information and so many messages are received that the most important ones cannot be easily identified and quickly acted on – most likely to occur with electronic media.
81.Communication barriers – reasons why communication fails
82.Formal communication networks – the official communication channels and routes used within an organisation
83.Informal communication – unofficial channels of communication that exists between informal groups within an organisation
84.Marketing plan – a detailed, fully researched written report on marketing objectives and the marketing strategy to be used to achieve them
85.Income elasticity of demand – measures the responsiveness of demand for a product following a change in consumer incomes
Income elasticity of demand = % change in demand for the product/% change in consumer incomes
86.Promotional elasticity of demand – measures the responsiveness of demand for a product following a change in the amount spent on promoting it
Promotional elasticity of demand = % change in demand for the product/% change in promotional spending
87.Cross elasticity of demand – measures the responsiveness of demand for a product following a change in the price of another product
88.New product development (NPD) – the design, creation and marketing of new goods and services
89.Test marketing – the launch of the product on a small-scale market to test consumers’ reactions to it
90.Research and development – the scientific research and technical development of new products and processes
91.Sales forecasting – predicting future sales levels and sales trends
92.Sales-force composite – a method of sales forecasting that adds together all of the individual predictions of future sales of all the sales representatives working for a business
93.Delphi method – a long-range qualitative forecasting technique that obtains forecasts from a panel of experts
94.Jury of experts – uses the specialists within a business to make forecasts for the future
95.The trend – the underlying movement in a time series
96.Seasonal fluctuations – the regular and repeated variations that occur in sales data within a period of 12 months

97.Cyclical fluctuations – these variations in sales occur over periods of time of much more than a year and are due to the business cycle
98.Random fluctuations – these can occur at any time and will cause unusual and unpredictable sales figures – examples include exceptionally poor weather or negative public image following a high-profile product failure
99.Globalisation – the growing trend towards worldwide markets in products, capital and labour, unrestricted by barriers
100.Multinational companies – businesses that have operations in more than one country
101.Free international trade – international trade that is allowed to take place without restrictions such as ‘protectionist’ tariff s and quotas
102.Tariff – tax imposed on an imported product
103.Quota – a physical limit placed on the quantity of imports of certain products
104.International marketing – selling products in markets other than the original domestic market
105.BRICS – the acronym for five rapidly developing economies with great market opportunities – Brazil, Russia, India, China and South Africa
106.Pan-global marketing – adopting a standardised product across the globe as if the entire world were a single market – selling the same goods in the same way everywhere
107.Global localisation – adapting the marketing mix, including differentiated products, to meet national and regional tastes and cultures
108.Capacity utilisation – the proportion of maximum output capacity currently being achieved
109.Excess capacity – exists when the current levels of demand are less than the full capacity output of a business – also known as spare capacity
110.Rationalisation – reducing capacity by cutting overheads to increase efficiency of operations, such as closing a factory or off ice department, often involving redundancies
111.Full capacity – when a business produces at maximum output Capacity shortage – when the demand for a business’s products exceeds production capacity
112.Outsourcing – using another business (a ‘third party’) to undertake a part of the production process rather than doing it within the business using the firm’s own employees
113.Business-process outsourcing (BPO) – a form of outsourcing that uses a third party to take responsibility for certain business functions, such as HR and finance

114.Lean production – producing goods and services with the minimum of wasted resources while maintaining high quality
115.Simultaneous engineering – product development is organised so that different stages are done at the same time instead of in sequence
116.Cell production – splitting flow production into self-contained groups that are responsible for whole work units
117.Kaizen – Japanese term meaning continuous improvement
118.Quality product – a good or service that meets customers’ expectations and is therefore ‘fit for purpose’
119.Quality standards – the expectations of customers expressed in terms of the minimum acceptable production or service standards
120.Quality control – this is based on inspection of the product or a sample of products
121.Quality assurance – a system of agreeing and meeting quality standards at each stage of production to ensure consumer satisfaction
122.ISO 9000 – this is an internationally recognised certificate that acknowledges the existence of a quality procedure that meets certain conditions
123.Total quality management – an approach to quality that aims to involve all employees in quality-improvement
124.Internal customers – people within the organisation who depend upon the quality of work being done by others
125.Zero defects – achieving perfect products every time
126.Benchmarking – involves management identifying the best firms in the industry and then comparing the performance standards – including quality – of these businesses with those of their own business
127.Project – a specific and temporary activity with a start and end date, clear goals, defined responsibilities and a budget
128.Project management – using modern management techniques to carry out and complete a project from start to finish in order to achieve pre-set targets of quality, time and cost
129.Critical path analysis – a planning technique that identifies all tasks in a project, puts them in the correct sequence and allows for the identification of the critical path
130.Critical path – the sequence of activities that must be completed on time for the whole project to be completed by the agreed date
131.Network diagram – the diagram used in critical path analysis that shows the logical sequence of activities and the logical dependencies between them – so the critical path can be identified

132.Cost centre – a section of a business, such as a department, to which costs can be allocated or charged
133.Profit centre – a section of a business to which both costs and revenues can be allocated – so profit can be calculated
134.Full costing – a method of costing in which all fixed and variable costs are allocated to products, services or divisions of a business
135.Contribution or marginal costing – costing method that allocates only direct costs to cost/profit centres, not overhead costs
136.Budget – a detailed financial plan for the future
137.Budget holder – individual responsible for the initial setting and achievement of a budget
138.Variance analysis – calculating differences between budgets and actual performance, and analysing reasons for such differences
139.Delegated budgets – giving some delegated authority over the setting and achievement of budgets to junior managers
140.Incremental budgeting – uses least year’s budget as a basis and an adjustment is made for the coming year
141.Zero budgeting – setting budgets to zero each year and budget holders have to argue their case to receive any finance
142.Flexible budgeting – cost budgets for each expense are allowed to vary if sales or production vary from budgeted levels
143.Adverse variance – exists when the difference between the budgeted and actual figure leads to a lower-than-expected profit
144.Favourable variance – exists when the difference between the budgeted and actual figure leads to a higher-than-expected profit
145.Intellectual property – the amount by which the market value of a firm exceeds its tangible assets less liabilities – an intangible asset
146.Market value – the estimated total value of a company if it were taken over
147.Capital expenditure – any item bought by a business and retained for more than one year, that is the purchase of fixed or non-current assets
148.Revenue expenditure – any expenditure on costs other than non-current asset expenditure
149.Depreciation – the decline in the estimated value of a noncurrent asset over time
Assets decline in value for two main reasons: normal wear and tear through usage & technological change, making either the asset, or the product it is used to make, obsolete

150.Net book value – the current Statement of financial position value of a non-current asset = original cost – accumulated depreciation
151.Straight-line depreciation – a constant amount of depreciation is subtracted from the value of the asset each year.
Straight line depreciation = original cost of asset-expected residual value/expected useful life of asset (years)
152.Net realisable value – the amount for which an asset (usually an inventory) can be sold minus the cost of selling it – it is only used on Statements of financial position when NRV is estimated to be below historical cost
153.Return on capital employed (%) – operating profit/capital employed × 100
154.Capital employed – the total value of all long-term finance invested in the business: it is equal to (non-current assets + current assets) − current liabilities or non-current liabilities + shareholders’ equity
155.Inventory turnover ratio – cost of goods sold/value of inventories
156.Day’s sales in receivables ratio – trade accounts receivable * 365/revenue
157.Share price – the quoted price of one share on the stock exchange Dividend – the share of the company profits paid to shareholders
158.Dividend yield ratio – dividend per share * 100/current share price
159.Dividend per share – total annual dividends/total number of issued shares
160.Dividend cover ratio – profit for the year/annual dividends
161.Price/earnings ratio – current share price/earnings per share
162.Earnings per share – profit for the year/annual dividends This is the amount of profit (after tax and interest) earned per share
163.Investment appraisal – evaluating the profitability or desirability of an investment project
164.Annual forecasted net cash flow – forecast cash inflows minus forecast cash outflows
165.Payback period – length of time it takes for the net cash inflows to pay back the original capital cost of the investment
166.Accounting rate of return – measures the annual profitability of an investment as a percentage of the initial investment
ARR (%) = annual profit (net cash flow)/initial capital cost × 100 An alternative formula is:
ARR (%) = annual profit (net cash flow)/average capital cost × 100 where the average capital cost = initial capital cost – residual capital value/2

167.Net present value (NPV) – today’s value of the estimated cash flows resulting from an investment
168.Internal rate of return (IRR) – the rate of discount that yields a net present value of zero – the higher the IRR, the more profitable the investment project is
169.Criterion rate or levels – the minimum levels (maximum for payback period) set by management for investment appraisal results for a project to be accepted
170.Corporate strategy – a long-term plan of action for the whole organisation, designed to achieve a particular goal
171.Tactic – short-term policy or decision aimed at resolving a particular problem or meeting a specific part of the overall strategy
172.Strategic management – the role of management when setting
long-term goals and implementing cross-functional decisions that should enable a business to reach these goals
173.Competitive advantage – a superiority gained by a business when it can provide the same value product/service as competitors but at a lower price, or can charge higher prices by providing greater value through differentiation
174.Strategic analysis – the process of conducting research into the business environment within which an organisation operates, and into the organisation itself, to help form future strategies
175.SWOT analysis – a form of strategic analysis that identifies and analyses the main internal strengths and weaknesses and external opportunities and threats that will influence the future direction and success of a business
176.PEST analysis – the strategic analysis of a firm’s macroenvironment, including political, economic, social and technological factors
177.Mission statement – a statement of the business’s core purpose and focus, phrased in a way to motivate employees and to stimulate interest by outside groups
178.Vision statement – a statement of what the organisation would like to achieve or accomplish in the long term
179.Boston Matrix – a method of analysing the product portfolio of a business in terms of market share and market growth
180.Core competence – an important business capability that gives a firm competitive advantage
181.Core product – product based on a business’s core competences, but not necessarily for final consumer or end user

182.Ansoff ’s matrix – a model used to show the degree of risk associated with the four growth strategies of market penetration, market development, product development and diversification
183.Market penetration – achieving higher market shares in existing markets with existing products
184.Product development – the development and sale of new products or new developments of existing products in existing markets
185.Market development – the strategy of selling existing products in new markets
186.Diversification – the process of selling different, unrelated goods or services in new markets
187.Force-field analysis – technique for identifying and analysing the positive factors that support a decision (‘driving forces’) and negative factors that constrain it (‘restraining forces’)
188.Decision tree – a diagram that sets out the options connected with a decision and the outcomes and economic returns that may result
189.Expected value – the likely financial result of an outcome obtained by multiplying the probability of an event occurring by the forecast economic return if it does occur
190.Strategic implementation – the process of planning, allocating and controlling resources to support the chosen strategies
191.Business plan – a written document that describes a business, its objectives and its strategies, the market it is in and its financial forecasts
192.Corporate plan – this is a methodical plan containing details of the organisation’s central objectives and the strategies to be followed to achieve them
193.Corporate culture – the values, attitudes and beliefs of the people working in an organisation that control the way they interact with each other and with external stakeholder groups
194.Task culture – based on cooperation and teamwork
195.Person culture – when individuals are given the freedom to express themselves fully and make decisions for themselves
196.Entrepreneurial culture – this encourages management and workers to take risks, to come up with new ideas and test out new business ventures
197.Power culture – concentrating power among just a few people
198.Role culture – each member of staff has a clearly defined job title and role

199.Change management – planning, implementing, controlling and reviewing the movement of an organisation from its current state to a new one
200.Business process re-engineering – fundamentally rethinking and redesigning the processes of a business to achieve a dramatic improvement in performance
201.Project champion – a person assigned to support and drive a project forward, who explains the benefits of change and assists and supports the team putting change into practice
202.Project groups – these are created by an organisation to address a problem that requires input from different specialists
203.Contingency plan – preparing an organisation’s resources for unlikely events

Unit 1 .Business and its environment (AS Level
Consumer goods – the physical and tangible goods sold to the general

public – include durable consumer goods like cars and washing machines and non-durable goods like food, drinks and sweets that can be used only once.
Consumer services – the non-tangible products sold to the general

public. It includes hotel accommodation, insurance services and train journeys.
Consumer – Individual who buys goods and services for their own use.

Customer – Individual, group of individuals or an organisation who purchase goods and services from a business.
Factor of Production – Resources required by business to commence production of goods and services.
Capital goods – the physical goods the industry uses to aid in producing other goods and services, such as machines and commercial vehicles.
Adding value – increasing the difference between the cost of purchasing bought-in materials and the price the finished goods are sold for.
Added value – the difference between the costs of purchasing bought-in materials and the price the finished goods are sold for.

Opportunity cost – the benefit of the next most desired option given up.

Entrepreneur – someone who takes the financial risk of starting and managing a new venture.
Enterprise – Action of showing initiatives to take risk to start up a business.
Branding – Process of differentiating or making a product unique relative to competitors by developing a symbol, name, image or trademark etc.
Multinational Business (MNC) – A business firm that has its head office in one nation, but with operating branches, factories in other countries.
Intrapreneur – Employee of the business who takes direct responsibility for turning an innovative idea into a profitable product or business
venture.

Business Plan – Written documents that describes a business, its objectives, strategies, financial forecast and the market it operates in.
Primary Sector Business Activity – Firms engaged in farming, fishing, oil extraction and all other industries that extract natural resources so that
they can be used and processed by other firms.
Secondary Sector Business Activity – Firms that manufacture and process products from natural resources including computers, brewing, baking, and clothes-making and construction.

Tertiary Sector Business Activity – Firms that provide services to consumers and other businesses such as retailing, transport, insurance,
banking, hotels, tourism and telecommunications.
Quaternary Sector Business Activity – Firms that provides information related services. It includes R&D, ICT, computing, web designing and management consultancy, etc.
Public Sector – It comprises of organisations accountable to and controlled by the central or local government.
Private Sector – It comprises of businesses owned and controlled by individuals or groups of individuals.
Mixed Economy – Economic resources are owned and controlled by private and public sectors.
Free-Market Economy – economic resources are owned largely by the private sector with little state intervention.
Command Economy – Economic resources are owned, planned and controlled by the state.
Sole Trader – A business in which one person provides the permanent finance and, in return, has full control of the business and can keep all of
the profits.

Partnership – A business formed by two or more people to carry on a business together, with shared capital investment and, usually, shared
responsibilities.
Limited Liability – The only liability or potential loss the shareholder has if the company fails is the amount invested in the company, not the total wealth of the shareholder.
Unlimited Liability – Founder or Owners of the business bear full, legal responsibility for debt of the business which can risk their personal
assets.
Private limited company – A small to medium-sized business owned by shareholders who are often members of the same family; this company cannot sell shares to the general public.
Share – A certificate confirming part ownership of a company and entitling the shareholder owner to dividends and certain shareholder
rights.

Shareholder – A person or institution owning shares in a limited company.
Public limited company – A limited company, often a large business, with the legal right to sell shares to the general public. Prices are quoted
on the national stock exchange.

Public corporation – A business enterprise owned and controlled by the state-also known as nationalised industry.
Memorandum of association – This states the name of the company, the address of the head office through which it can be contacted, the
maximum share capital for which the company seeks authorisation and the declared aims of the business.
Articles of association – This document cover the internal working and

control of the business-for example, the names of the directors and the procedures to be followed at meetings will be detailed.
Cooperative – Jointly owned business whose members operate it

considering their mutual benefits, to produce or distribute goods and services. E.g. Consumers' cooperative, Farmers' cooperative and Workers' cooperative, etc.
Franchise – A business that uses the name, logo and trading systems of

an existing successful business.
Franchiser – Person or Business selling license containing rights of their brand image, name or identity to someone who wants to open shops and sell products under that brand identity.
Franchisee – Person or Business purchasing license that contains rights to operate under, usually a successful established brand.

Joint Venture – When two or more firms agree to work closely together on a particular project and establish a completely separated business
division to commence operation of that project.

Social Enterprise – A business with mainly social objectives that injects most of its profit back into the business with aims based on societal
welfare rather than profit motive. They following the triple bottom line.

Triple Bottom Line – Three objectives of social enterprise:- Economic (Financial), Social and Environmental.
Revenue – Total value of sales made during a certain time period of business operation.
Capital Employed – Total value of long-term finance invested into a business.
Market Capitalisation – Total value of issued shares of the business firm.

Market Share – Sales of a business as a proportion of total market sales.
Small Business – A business with a limited scale of operations. Its characteristics consist of having fewer employees and lower revenue compared to large enterprises. Such businesses are usually privately owned and operated.
Family Business – A business where decision-making process occurs with members of a family. It is typically managed and controlled by family

members across multiple generations, with family interests influencing its operation and strategy.
Organic Growth – Expansion of a business by establishing new plants,

stores, or factories. Also known as internal growth.

External Growth – Expansion of a business through integration or takeover of another business.
Merger – Agreement by owners and managers of two businesses to unite them together into a new combined business. It's referred to as friendly
merger.

Takeover – When a company buys more than 50% of shares of another business and becomes its owner. Also known as acquisition.
Horizontal Merger – Integration with a business in the same industry in the same stage of production.
Vertical Integration – Integration with a business in the same industry in different stage of production.
Backward Vertical Integration – Integration with a business in the same industry in the earlier stage of production. It integrates with supplier
business.
Forward Vertical Integration – Integration with a business in the same industry in the later stage of production. It integrates with retailer business.

Conglomerate Integration – Integration with a business in the different industry in the different stage of production.
Synergy – "The whole is greater than the sum of parts". It is usually

assumed that combined business organisations are more successful than its original separate entities.
Strategic Alliance – Agreement between two firms to commit resources

to accomplish a certain aim while retaining its independence from each other.
Business Objectives – A stated measurable target of the business written

in its business plan that it hopes to achieve.
Corporate Social Responsibility (CSR) – When businesses take interest of the society in consideration, and by taking accountability for the impact of their decisions and activities on various stakeholders as well as the environment.
Pressure Group – An association created by group of individuals with a common interest or goal, thus putting pressure on corporations and
government to change specific policies so that their aim is achieved. It is usually for betterment of society.
SMART Objectives – Aims that are specific, measurable, achievable,

realistic and time-limited.

Annual (Company) Report – Document containing details of a firm's activities over a year, including its financial accounts.
Business Strategy – Long-term plan consisting steps of action of a business, tailored to achieve a specific objective.
Tactic – Short-term plan of action which is a part of the overall strategy to achieve its main aim.
Target – Short-term objective of the corporation that must be completed in order to achieve their overall objective.
Ethical Code (Code of Conduct) – Document detailing company's rules and guidelines on employee behaviour that must be followed by all the
workers.

Stakeholders – Individuals or groups who can be affected by, and have an interest in, any action taken by an organisation.
External Stakeholders – Individuals or groups who are separate from the business but are affected by or interested in its operations.
Internal Stakeholders – Individuals or groups who work within the business, or own it, and are affected by the operations of the business.
Trade Union – Organisations of working people with the objective of improving the pay and working conditions of its members and providing
them with support and legal services.

Stakeholder Concept – The view that businesses and their managers

have responsibilities to a wide range of groups, not just shareholders. Also known as stakeholder theory.


Unit 2 -Human resource management (AS Level)
Human Resource Management (HRM) – The strategic approach to managing employees so they help the business succeed.
Workforce Planning – Predicting how many workers and what skills will be needed to meet company goals.
Workforce Audit – Checking the skills and qualifications of current employees and managers.
Labour Turnover – The rate at which employees leave a company.

Recruitment – Finding and attracting people to fill a job position.

Selection – The steps taken to interview, test, and choose the right candidate for a job.
Recruitment Agency – A business that helps companies find candidates for job openings.
Job Description – A list of the main tasks and responsibilities of a job.

Person Specification – A list of the skills, qualities, and qualifications needed for a job.

Curriculum Vitae (CV) – A detailed document showing a person’s education, work experience, and achievements.
Resume – A shorter document summarizing work experience, education, and skills relevant to the job.
Reference – A recommendation or comment about an applicant’s character or past work performance.
Assessment Centre – A place where job candidates are tested on their abilities to perform a role.
Internal Recruitment – Filling a job from within the current employees of the business.
External Recruitment – Hiring someone from outside the company for a job.
Employment Contract – A legal document outlining the terms of a worker’s job.
Redundancy – When a job is no longer needed, and the employee is let go.
Dismissal – Being fired from a job due to poor performance or breaking rules.
Unfair Dismissal – Being fired for a reason that is not legally justified.

Employee Morale – The overall mood and satisfaction of employees at work.

Employee Welfare – The health, safety, and wellbeing of employees in the workplace.
Work-Life Balance – Managing time and effort between work and personal life.
Equality Policy – Rules to ensure everyone is treated fairly and has equal opportunities.
Diversity Policy – Policies to create a diverse workforce and value differences.
Training – Work-related education to improve skills and efficiency.

Induction Training – Training to introduce new employees to the company and its systems.
On-the-Job Training – Training given at the workplace while doing the job.
Off-the-Job Training – Training done away from the workplace.

Multi-skilling – Training employees in multiple skills for more flexibility.

Employee Appraisal – Evaluating an employee’s performance based on set goals.
Industrial Action – Workers taking action to pressure management during a dispute.

Collective Bargaining – Negotiating working conditions between a group of employees who are usually represented by trade union officials and
their employer.

Trade Union Recognition – When a company agrees to negotiate with a trade union instead of individual workers.
Motivation – The internal and external factors that stimulate the desire in workers to stay interested in and committed to doing a job well.
Self-Actualisation – A sense of self-fulfillment achieved through learning and accomplishments.
Job Enrichment – Using the full capabilities of workers by giving them more challenging and fulfilling tasks.
Piece Rate – Payment to a worker for each unit produced.

Time-Based Wage Rate – Payment made to a worker for each period of time worked.
Salary – Annual income, typically paid monthly.

Commission – Payment to a salesperson for each sale made.

Bonus – An additional payment on top of the agreed wage or salary.

Performance-Related Pay – A bonus scheme that rewards employees for above-average work performance.
Profit Sharing – A bonus given to employees based on company profits, usually as a proportion of their salary.

Share-Ownership Scheme – A program that gives employees shares in the company or allows them to buy shares at a discount.
Fringe Benefits – Additional perks given by an employer, separate from regular pay.
Job Rotation – A system where employees switch between different jobs.

Job Enlargement – Expanding a job by broadening or deepening the tasks undertaken.
Job Redesign – Restructuring a job to make it more interesting, satisfying, and challenging.
Development – Gaining new or advanced skills and knowledge, with opportunities to apply them.
Employee Participation – Actively involving employees in decision-making within the company.
Teamworking – Organizing production so groups of workers complete entire units of work together.
Empowerment – Providing employees with the skills, resources, authority, and opportunities to make decisions and be responsible for
their work.

Quality Circle (QC) – A voluntary group of workers who meet regularly to discuss and solve work-related problems.

Manager – The person responsible for setting goals, organizing resources, and motivating workers to achieve business objectives.
Management – The coordination and organization of activities to accomplish the business's defined goals.
Autocratic Management – A style where one manager makes all decisions with little to no input from others.
Paternalistic Management – A style where the manager assumes they know what is best for the organization, similar to a parental figure.
Laissez-Faire Management – A style where most business decisions are left to the workforce.
Democratic Management – A style that encourages workers to actively participate in decision-making.
Theory X – The belief that some managers hold, thinking employees are lazy, need constant supervision, and are motivated by fear.
Theory Y – The belief that some managers hold, thinking employees are self-motivated, enjoy their work, and are willing to take on extra
responsibilities.

Unit 3 - Marketing (AS Level)

Marketing Objectives – The goals set for the marketing department to help the business achieve its overall company objectives.

Marketing – The management task of identifying and satisfying customer needs profitably by delivering the right product at the right price, place,
and time.

Corporate Objectives – Clear and realistic goals set for the entire company.
Marketing Strategy – A detailed plan of action that outlines how a business will achieve its marketing goals and gain a competitive
advantage.

Equilibrium Price – The price at which the quantity demanded by consumers equals the quantity supplied by producers.
Demand – The amount of a product that consumers are willing and able to buy at a specific price during a certain time period.
Supply – The amount of a product that businesses are willing to offer at a specific price during a certain time period.
Market Segment – A smaller group within a larger market where consumers share similar characteristics.
Industrial Market – The market for products sold by businesses to other businesses (B2B).
Consumer Market – The market for products sold by businesses to individual consumers (B2C).

Customer/Market Orientation – An approach that focuses on making product decisions based on consumer demand identified through market
research.
Product Orientation – An approach that focuses on producing products that a company can make or has traditionally made, and then trying to sell them.
Market Size – The total value or volume of sales in a market over a specific time period.
Market Growth – The percentage increase in the total market size (by volume or value) over a given period.
Brand Leader – The brand with the largest market share.

Consumer Products – Goods or services sold directly to end users.

Industrial Products – Goods or services sold to other businesses.

Mass Marketing – Selling standardized products to the entire market without differentiation.
Niche Marketing – Identifying a small segment of a larger market and offering products tailored specifically to that segment.
Market Segmentation – Dividing a market into distinct customer groups with common needs and marketing different products to each group.
Consumer Profile – A detailed picture of a business's consumers, showing their age, income, location, gender, and social class.

Customer Relationship Marketing (CRM) – Using marketing strategies to build strong relationships with customers, ensuring loyalty and repeat
business.

Market Research – The process of gathering, recording, and analyzing information about customers, competitors, and the market.
Primary Research – Collecting original, first-hand data directly related to the business’s needs.
Secondary Research – Using existing data that was collected for a different purpose.
Qualitative Data – Non-numerical data that gives insight into the motivations and behaviors of consumers.
Quantitative Data – Numerical data from research that can be analyzed statistically.
Sampling – Selecting a group of respondents from a larger population for research purposes.
Sample – A selected group of people participating in market research, representing the broader target market.
Sampling Bias – When the chosen sample doesn’t accurately represent the entire population, giving some people a higher chance of being
selected.

Arithmetic Mean – The average value calculated by adding up all the data points and dividing by the number of points.
Mode – The value that appears most frequently in a data set.

Median – The middle value in an ordered set of data, dividing it into two equal halves.
Range – The difference between the highest and lowest values in a data set.
Coding – The process of labelling and organising qualitative data to identify the main themes and the links between them.
Marketing Mix – The four key decisions—product, price, promotion, and place—that ensure effective marketing of a product.
Product – Goods or services created during the production process and sold to meet customer needs.
Goods – Physical products like cars or soap bars.

Services – Non-physical products that fulfill customer needs, like teaching, plumbing, or banking.
Brand – A unique name, symbol, or trademark that distinguishes a product from its competitors.
Intangible Attributes – Qualities of a product that are based on customer opinions and are difficult to measure or compare.

Tangible Attributes – Measurable features of a product that can easily be compared with others.
Unique Selling Point (USP) – A distinctive feature of a product that sets it apart from competitors.
Product Differentiation – The unique qualities of a product that make it stand out from competitors.
Product Positioning – How consumers perceive a product compared to its competitors.
Product Portfolio Analysis – Reviewing a business’s range of products to decide how best to allocate resources.
Product Life Cycle – The stages of a product's sales from launch to withdrawal from the market.
Consumer Durable – A product designed for reuse with a long lifespan, like a car or washing machine.
Extension Strategy – A plan to extend the maturity phase of a product’s life before launching a new one.
Boston Matrix – A tool for analyzing a company’s product range in terms of market share and growth.
Mark-Up Pricing – Adding a fixed profit margin to the cost of a product to set its price.

Cost-Plus Pricing – Setting a price by calculating the unit cost and adding a set profit margin.
Contribution-Cost Pricing – Pricing based on variable costs to contribute to fixed costs and profit.
Competitive Pricing – Setting prices based on what competitors are charging.
Price Discrimination – Charging different prices to different customer groups for the same product or service.
Dynamic Pricing – Adjusting prices based on demand and customers’ willingness to pay.
Penetration Pricing – Setting a low price to encourage high sales volume.

Price/Market Skimming – Charging a high price for a new product with low price sensitivity due to uniqueness.
Psychological Pricing – Setting prices to align with customers’ perceived value of a product.
Promotion – The use of various methods like advertising, sales promotions, personal selling, direct mail, trade fairs, sponsorships, and
public relations to inform and persuade consumers to make a purchase.

Advertising – Paid communication using platforms such as TV, newspapers, and cinemas to inform and convince customers.

Direct Promotion – A variety of promotional efforts targeting specific consumers directly, often referred to as direct marketing.
Sales Promotion – Offering special deals and incentives to consumers or retailers to boost short-term sales and encourage repeat purchases.
Promotion Mix – The blend of promotional strategies a company uses to market its products.
Digital Promotion – Marketing and promoting products using digital platforms, primarily on the internet but also via mobile devices.
E-commerce – Conducting transactions for buying and selling goods and services through online platforms.
Channel of Distribution – The network of intermediaries that a product goes through from the producer to the final consumer.
Online Marketing (E-commerce) – Using the internet, email, and mobile communications for selling and marketing products directly through
electronic commerce.

Digital Distribution – The delivery of digital media content such as music, videos, software, and games over the internet.
Physical Distribution – The processes involved in moving finished products efficiently from the production facility to the consumer.

Integrated Marketing Mix – Ensuring that all marketing decisions and strategies align with one another to deliver a clear and consistent
message to consumers about the product.
Intellectual Capital – The intangible assets of a business, including human capital (skilled employees), structural capital (information systems and databases), and relational capital (strong relationships with suppliers and customers).
Unit 4 - Operations management (AS Level)
Transformational Process – Activities that convert inputs into outputs, adding value during the process to produce goods or services for customers.
Productivity – The measure of output generated from a given set of inputs, such as output per worker over a specific time period.
Level of Production – The total number of units produced within a certain time frame.
Production – The process of turning inputs, like raw materials and labor, into finished products or services.
Efficiency – The ability to produce outputs at the highest ratio of output to input.
Effectiveness – Achieving business goals by utilizing inputs in a way that meets customer needs and business objectives.

Sustainability of Operations – Maintaining business practices over the long term by ensuring environmental protection and preserving the
quality of life for future generations.

Labour Intensive – A production process that requires a high amount of labor compared to the use of capital equipment.
Capital Intensive – A production process that relies heavily on machinery and equipment rather than labor input.
Job Production – The creation of a unique product that is specifically designed to meet an individual customer's needs.
Batch Production – Producing a set of identical items in groups, where each product passes through stages of production simultaneously.
Flow Production –Continuous production where products are made in an ongoing process without interruption.
Mass Customisation – The use of advanced, flexible technology in production lines to create personalized products according to individual
customer preferences.

Inventory – Materials and goods that a business keeps on hand to enable production and meet customer demand.
Inventory Management – The process of managing the ordering, storage, and use of a company's inventory.

Economic Order Quantity – The most cost-effective quantity of stock to reorder, balancing delivery and storage costs.
Buffer Inventory – The minimum amount of stock that must be kept to ensure uninterrupted production in case of supply delays or sudden
increases in demand.

Re-order Quantity – The number of units ordered every time a new stock order is placed.
Lead Time – The duration between placing an order for supplies and receiving the delivery.
Re-order Level – The inventory level at which a new order is triggered to avoid running out of stock.
Supply Chain – The interconnected system of businesses and activities involved in the production and distribution of a product, from raw
materials to the final delivery to the customer.
Supply Chain Management – Managing the entire process from sourcing raw materials to delivering the finished product, aiming to minimize costs while improving customer service.
Just-in-Time (JIT) Inventory Management – A strategy that avoids holding stock by ensuring materials arrive just as needed for production
and that finished goods are made to order.

Just-in-Case (JIC) Inventory Management – A strategy that reduces the risk of stock shortages by maintaining higher levels of buffer inventory.
Maximum (Full) Capacity – The highest level of output a business can consistently achieve over time.
Capacity Utilisation – The percentage of the maximum output capacity that is currently being used.
Outsourcing – Hiring another business to handle part of the production process instead of doing it in-house with the company's employees.
Excess Capacity – It occurs when current output levels are lower than the business's full production capacity, also called spare capacity.
Rationalisation – The process of cutting capacity by shutting down factories or production units.
Capacity Shortage – When the demand for a company's products surpasses its production capacity.
Business Process Outsourcing (BPO) – A type of outsourcing where

specialized contractors manage specific business functions like human resources or finance.


Unit 5 -Finance and accounting (AS Level)
Start-up Capital – The initial capital required by an entrepreneur to establish a business.

Working Capital – Funds needed to cover raw materials, day-to-day expenses, and credit extended to customers.
Short-term Finance – Finance needed for periods of up to one year.

Long-term Finance – Finance required for periods longer than one year.

Profit – The surplus remaining after all costs have been subtracted from total revenue.
Liquidity – The ability of a business to meet its short-term financial obligations.
Administration – When external administrators manage a business that cannot pay its debts, with the intention of selling it as a going concern.
Bankruptcy – A legal procedure that involves liquidating a business or property to pay off debts.
Liquidation – When a business stops trading and sells its assets to pay creditors.
Current Assets – Assets that are cash or can be converted to cash within a year, such as inventory or trade receivables.
Current Liabilities – Debts or obligations that are due to be paid within one year.
Capital Expenditure – The purchase of long-term assets, like machinery or buildings, expected to last for more than one year.

Revenue Expenditure – Spending on operational costs and short-term assets, such as wages and inventory.
Retained Earnings – Profit kept in the business after taxes, rather than being paid out as dividends.
Internal Sources – Finance raised from within the business, such as from retained earnings or the sale of assets.
External Sources – Finance raised from outside the business, such as loans or investments from banks.
Non-current Assets – Long-term assets held and used by the business for more than one year.
Overdraft – A pre-arranged credit limit with a bank that allows a business to borrow money as needed.
Factoring – Selling accounts receivable to a third party in exchange for immediate cash.
Hire Purchase – A method of buying an asset with fixed payments over time, with ownership transferred after the final payment.
Leasing – Renting an asset for a fixed period, avoiding the need for long-term capital to purchase the asset outright.
Long-term Loans – Loans that do not need to be repaid for at least one year.

Debentures – Long-term bonds issued by companies to raise finance, often with a fixed interest rate.
Share (Equity) Capital – Permanent finance raised by selling shares in the business.
Business Mortgages – Long-term loans secured against a property used for business purposes.
Venture Capital – Risk capital invested in start-ups or small businesses with high growth potential.
Collateral Security – An asset pledged to a lender that may be sold to repay a loan if the borrower defaults.
Rights Issue – An offer to existing shareholders to purchase additional shares at a discounted price.
Microfinance – Financial services provided to individuals or small businesses who lack access to traditional banking services.
Crowd Funding – Raising small amounts of capital from a large number of people to finance a new business or project.
Cash Flow – The net balance of cash moving into and out of a business.

Insolvent – When a business cannot meet its short-term debts.

Cash Flow Forecast – An estimate of future cash inflows and outflows.

Cash Inflow – Money in form of note received by a business.

Cash Outflow – Money in form of cash spent by a business.

Net Cash Flow – The difference between cash inflows and outflows over a given period.
Opening Cash Balance – The amount of cash a business holds at the beginning of a period.
Closing Cash Balance – The amount of cash held at the end of a period, which becomes the opening balance for the next period.
Credit Control – Monitoring customer debts to ensure they are paid within the agreed time frame.
Bad Debt – Unpaid bills that are unlikely to be collected.

Overtrading – Expanding a business too quickly without sufficient finance, leading to cash flow problems.
Cost Centre – A department or section of a business that incurs costs but does not generate revenue.
Direct Costs – Costs directly linked to the production of goods and services.
Indirect Costs – Costs that cannot be directly allocated to a specific unit of production.
Fixed Costs – Costs that remain unchanged regardless of output in the short term.
Variable Costs – Costs that vary depending on the level of output.

Total Cost – The sum of fixed and variable costs.

Profit Centre – A division of a business to which both revenues and costs are assigned, allowing profit calculation.
Average Cost – The total cost divided by the number of units produced.

Full Costing – A costing method that assigns all direct and indirect costs to products or divisions.
Contribution Per Unit – The price of a product minus its variable costs.

Break-even Point – The output level at which total revenue equals total costs, resulting in neither profit nor loss.
Break-even Analysis – The process of calculating the break-even point using cost and revenue data.
Margin of Safety – The difference between actual output and the break-even output level.
Budgeting – Planning future financial activities by setting performance targets.
Budget Holder – The individual responsible for setting and managing a budget.
Variance Analysis – The process of comparing actual results to the budgeted figures and analyzing the differences.
Delegated Budgets – Budgets for which junior managers are given responsibility for setting and achieving targets.

Incremental Budgeting – A budgeting method that uses the previous year's budget as a starting point, with adjustments for the current year.
Zero Budgeting – A budgeting method where every expense must be justified, and no funds are allocated automatically.
Favourable Variance – A change from the budget that results in higher-than-expected profit.
Flexible Budgeting – A budgeting approach that allows for cost adjustments if sales or output levels change.
Adverse Variance – A change from the budget that results in lower-than-expected profit.



MARKING GUIDANCE (9609):
- Knowledge (AO1): Define terms accurately.
- Application (AO2): Apply concepts to the specific case study/scenario.
- Analysis (AO3): Explain causes, consequences, and impacts (use connective words like "this leads to").
- Evaluation (AO4): Make judgments, weigh pros/cons, and conclude with justification.

CAMBRIDGE AS/A2 LEVEL BUSINESS (9609) - MARKING SCAFFOLD FOR 8 MARK QUESTIONS

Paragraph 1 - Analysis of Point 1

[Knowledge] Make your first point (briefly and precisely state one point to start your argument).
[App] For example… (Give a real business example if no context is provided or use the context if provided).
[MSAn] Which leads to…
[MSAn] Therefore…
[MSAn] Consequently…

Paragraph 2 - Analysis of Point 2

[Knowledge] Make your second point (briefly and precisely state one point to start your argument).
[App] For example… (Give a real business example if no context is provided or use the context if provided).
[MSAn] Which leads to…
[MSAn] Therefore…
[MSAn] Consequently…

MSAn = multi-stranded analysis.

CAMBRIDGE AS/A2 LEVEL BUSINESS (9609) - MARKING SCAFFOLD FOR 12 MARK QUESTIONS

Paragraph 1 - Introduction
1. Demonstrate relevant knowledge of any relevant concept or theory related to the question;
2. State or hint your conclusion.

Paragraph 2 - Analysis of an Individual Element
[Knowledge] Make your point (briefly and precisely state one point to start your argument).
[App+MSAn] This means that…
[App+MSAn] Which leads to…
[Evaluation] However... (Briefly and precisely state one counterpoint to your argument.)
[App+MSAn] This means that…
[App+MSAn] Which leads to…
[Heavy App] It can be concluded that the answer to the question is…
(*Mini-Conclusion* This conclusion is based on the argument you just discussed.)

Paragraph 3 - Analysis of Another Individual Element

[Knowledge] Make your point (briefly and precisely state one point to start your argument).
[App+MSAn] This means that…
[App+MSAn] Which leads to…
[Evaluation] However... (Briefly and precisely state one counterpoint to your argument.
[App+MSAn] This means that…
[App+MSAn] Which leads to…
[Heavy App] It can be concluded that the answer to the question is… (*Mini-Conclusion * This is based on the argument you just discussed.)

Paragraph 4 - Conclusion
1. Actual answer to the question.
2. In my opinion…
3. Cancel out a previous counterargument made.
4. Although I said…
5. My main reason for choosing this option is… (Justification: make the strongest possible point that supports your opinion.)
6. However, my decision would depend on… (Depending factor.)

CAMBRIDGE AS/A2 LEVEL BUSINESS (9609) - MARKING SCAFFOLD FOR 20 MARK QUESTIONS

Paragraph 1 - Introduction
1. Demonstrate relevant knowledge of any relevant concept or theory related to the question;
2. State or hint your conclusion.

Paragraph 2 - Analysis of an Individual Element
1. Make your point (briefly and precisely state one point to start your argument).
2. [App+MSAn] This means that…
3. [App+MSAn] Which leads to…
4. [Evaluation] However… (Briefly and precisely state one counterpoint to your argument.)
5. [App+MSAn] This means that…
6. [App+MSAn] Which leads to…
7. [Heavy App] It can be concluded that the answer to the question is… (*Mini-Conclusion* This is based on the argument you just discussed.)

Paragraph 3 - Analysis of Another Individual Element
1. Make your point (briefly and precisely state one point to start your argument).
2. [App+MSAn] This means that…
3. [App+MSAn] Which leads to…
4. [Evaluation] However… (Briefly and precisely state one counterpoint to your argument.)
5. [App+MSAn] This means that…
6. [App+MSAn] Which leads to…
7. [Heavy App] It can be concluded that the answer to the question is… (*Mini-Conclusion* This is based on the argument you just discussed.)

Paragraph 4 - Analysis of Overall Point of The Question
1. Make your point (briefly and precisely state one point to start your argument).
2. [App+MSAn] This means that…
3. [App+MSAn] Which leads to…
4. [Evaluation] However... (Briefly and precisely state one counterpoint to your argument.)
5. [App+MSAn] This means that…
6. [App+MSAn] Which leads to…
7. [Heavy App] It can be concluded that the answer to the question is… (*Main-Conclusion* This is based on the argument you just discussed.)

Paragraph 5 - Conclusion
Actual answer to the question.
1. In my opinion… (Actual answer to the question.)
2. Although I said... (Cancel out a previous counterargument made.)
3. My main reason for choosing this option is… (Justification: make the strongest possible point that supports your opinion.)
4. However, my decision would depend on… (Depending factor to ponder and show that you understand the alternative is possible in other circumstances).


"""
# ==========================================

# 🟢 CONFIGURATION
TEACHER_PIN = "3596" 
# You can hardcode the API key here if you want students to use yours, 
# or leave it empty to force them to enter one (not recommended for students).
# Example: HARDCODED_KEY = "AIzaSy..."
HARDCODED_KEY = "" 

st.set_page_config(page_title="Business Tutor", page_icon="🎓")

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your Cambridge Business tutor. Ask me anything about the syllabus."}]

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Settings")
    
    # API Key Handling
    if HARDCODED_KEY:
        api_key = HARDCODED_KEY
        st.success("API Key active (Teacher provided)")
    else:
        api_key = st.text_input("Enter Google API Key", type="password")
        if not api_key:
            st.warning("Please enter an API Key to start.")

    st.divider()
    
    # Teacher Dashboard in Sidebar
    with st.expander("👨‍🏫 Teacher Dashboard"):
        pin = st.text_input("Enter PIN", type="password")
        if pin == TEACHER_PIN:
            st.success("Unlocked")
            st.info(f"Loaded Content: {len(PERMANENT_SYLLABUS)} characters")
        elif pin:
            st.error("Incorrect PIN")

# --- MAIN CHAT LOGIC ---
if prompt := st.chat_input("Ask a question..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    if not api_key:
        st.error("Missing API Key.")
    else:
        try:
            genai.configure(api_key=api_key)
            # Auto-select model logic could go here, defaulting to flash for speed
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            system_instruction = f"""
            You are a Cambridge Business (9609) Tutor.
            
            CONTEXT (SYLLABUS):
            {PERMANENT_SYLLABUS}
            
            INSTRUCTIONS:
            1. Answer strictly using the CONTEXT provided.
            2. If the user asks for a definition, explain clearly.
            3. If the user asks for an essay answer, provide a STRUCTURE/OUTLINE only. Do not write the full essay.
            """
            
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = model.generate_content(f"{system_instruction}\n\nStudent Question: {prompt}")
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display Message History
for msg in st.session_state.messages:
    if msg["role"] != "user" and msg != st.session_state.messages[-1]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
