#!/bin/bash
# PickOps Stack Directory - Alphabetical Index

echo "=================================================="
echo "           PickOps - All Available Stacks"
echo "=================================================="
echo ""
echo "Total Stacks: 97"
echo ""

cat << 'EOF'
1.  AgentOps         - AI Agent Operations
2.  AgriOps          - Agriculture Operations
3.  AIOps            - AI Operations
4.  AirOps           - Airport Operations
5.  ALMOps           - Application Lifecycle Management
6.  AnimOps          - Animals & Plants Operations
7.  AppOps           - Application Operations
8.  ArchiOps         - Archaeology Operations
9.  AutoOps          - Automotive Operations
10. AviOps           - Aviation Operations
11. AWSOps           - AWS Operations
12. AzureOps         - Azure Operations
13. BankOps          - Banking Operations
14. BizOps           - Business Operations
15. BlockchainOps    - Blockchain Operations
16. ChemiOps         - Chemistry Operations
17. CivilOps         - Civil Engineering Operations
18. CodeOps          - Code Operations
19. CommOps          - Communications Operations
20. CompOps          - Computer Operations
21. ConstOps         - Construction Operations
22. DairyOps         - Dairy Operations
23. DataMeshOps      - Data Mesh Operations
24. DataOps          - Data Operations
25. DDDOps           - Domain-Driven Design Operations
26. DefOps           - Defence Operations
27. DevOps           - Development Operations
28. DevSecOps        - Development Security Operations
29. DrugOps          - Pharmaceutical Operations
30. EduOps           - Education Operations
31. ElderOps         - Elder Care Operations
32. ElectOps         - Electronics Operations
33. EnerOps          - Energy Operations
34. EnterOps         - Entertainment Operations
35. EventOps         - Event-Driven Operations
36. FarmOps          - Farm Operations
37. FinOps           - Financial Operations
38. FishOps          - Fishing Operations
39. FoodOps          - Food Operations
40. ForesOps         - Forest Operations
41. FurnOps          - Furniture Operations
42. GenAIOps         - Generative AI Operations
43. GitOps           - Git-based Operations
44. GovOps           - Government Operations
45. HealthOps        - Healthcare Operations
46. HomeOps          - Home Operations
47. HumanOps         - Human Resources Operations
48. HygenOps         - Hygiene Operations
49. InterOps         - Internet Operations
50. IoTOps           - IoT Operations
51. ITOps            - IT Operations
52. KidsOps          - Children Operations
53. LambdaOps        - Serverless Operations
54. LandOps          - Land Management Operations
55. LawOps           - Legal Operations
56. LLMOps           - Large Language Model Operations
57. LogiOps          - Logistics Operations
58. LoveOps          - Relationship Operations
59. MachiOps         - Machinery Operations
60. ManuOps          - Manufacturing Operations
61. MariOps          - Maritime Operations
62. MediOps          - Medical Operations
63. MicroservicesOps - Microservices Operations
64. MLOps            - Machine Learning Operations
65. MoneyOps         - Money Operations
66. MuniOps          - Municipality Operations
67. MusicOps         - Music Operations
68. NationOps        - Nation Operations
69. PetOps           - Pet Operations
70. PoliOps          - Politics Operations
71. PoultryOps       - Poultry Operations
72. PsychOps         - Psychology Operations
73. PubOps           - Media & Journalism Operations
74. QualiOps         - Quality Operations
75. RAGOps           - Retrieval-Augmented Generation Operations
76. RealOps          - Real Estate Operations
77. ReliOps          - Religion Operations
78. ResearOps        - Research Operations
79. RetaiOps         - Retail Operations
80. SagaOps          - Saga Pattern Operations
81. SciOps           - Science Operations
82. SecOps           - Security Operations
83. ServiceMeshOps   - Service Mesh Operations
84. ServOps          - Domestic Services Operations
85. SocioOps         - Social Living Operations
86. SpaceOps         - Space Operations
87. SporOps          - Sports Operations
88. TaxOps           - Taxation Operations
89. TechnoOps        - Technology Operations
90. TradeOps         - Trade Operations
91. TransOps         - Transportation Operations
92. WASMOps          - WebAssembly Operations
93. WastOps          - Waste Management Operations
94. WaterOps         - Water Operations
95. WearOps          - Apparel Operations
96. Web3Ops          - Web3 Operations
97. WebOps           - Web Operations
98. WomenOps         - Women Services Operations
99. WorkOps          - Employment Operations

=================================================="
Quick Start for Any Stack:
   cd [StackName]
   cp .env.example .env
   docker-compose up -d

Management:
   ./manage.sh [stackname] start
   make start STACK=[stackname]

Documentation:
   See README.md in each stack directory
   See STACKS_CATALOG.md for complete catalog
==================================================
EOF
