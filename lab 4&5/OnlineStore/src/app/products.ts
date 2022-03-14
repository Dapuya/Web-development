export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  url: string;
  rating: number;
  amazonURL: string;
}

export const products = [
  {
    id: 1,
    name: 'LEGO Star Wars Ultimate Millennium Falcon 75192 Expert Building Kit and Starship Model',
    price: 899.99,
    description: 'Defend the Galaxy and build the largest LEGO Star Wars Millennium Falcon to date! The perfect set for adult Star Wars fans and expert builders, This starship will inspire hours of play recreating the films or can be displayed as a collectible toy model',
    url: 'https://m.media-amazon.com/images/I/91FoS63ClXL._AC_SL1500_.jpg',
    rating: 4.9,
    amazonURL: 'https://www.amazon.com/LEGO-Ultimate-Millennium-Falcon-Building/dp/B075SDMMMV/ref=sr_1_4?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-4',
  },
  {
    id: 2,
    name: 'LEGO Creator Expert 10276 Colosseum (9036pcs)',
    price: 699,
    description: 'Bring to life your own brick-built model of the mighty Colosseum with this engaging and rewarding LEGO Colosseum (10276) model kit for adults. ',
    url: 'https://m.media-amazon.com/images/I/719ekgytasL._AC_SL1200_.jpg',
    rating: 4.4,
    amazonURL: 'https://www.amazon.com/LEGO-Creator-10276-Colosseum-9036pcs/dp/B08P11X1HX/ref=sr_1_5?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-5',
  },
  {
    id: 3,
    name: 'LEGO Ideas Old Fishing Store (21310) - Building Toy',
    price: 399.99,
    description: 'Build the LEGO Ideas Old Fishing Store, with detailed exterior, shop and connected lookout tower with office. Exterior features steps to the front and side doors of the store, railings, ventilator and assorted elements!',
    url: 'https://m.media-amazon.com/images/I/71Jl9dG1ROL._AC_SL1000_.jpg',
    rating: 4.9,
    amazonURL: 'https://www.amazon.com/LEGO-Ideas-Fishing-Store-21310/dp/B07198M22F/ref=sr_1_6?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-6',
  },
  {
    id: 4,
    name: 'LEGO Star Wars: The Mandalorian The Razor Crest 75292 Exclusive Building Kit, New 2020 (1,023 Pieces)',
    price: 279.99,
    description: 'Kids can role-play as heroic warrior The Mandalorian and play out action-packed Star Wars: The Mandalorian scenes with this detailed, LEGO brick model of The Razor Crest (75292) starship',
    url: 'https://m.media-amazon.com/images/I/918CAx5r5PL._AC_SL1500_.jpg',
    rating: 4.5,
    amazonURL: 'https://www.amazon.com/LEGO-Star-Wars-Mandalorian-Exclusive/dp/B0849GZMZH/ref=sr_1_7?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-7',
  },
  {
    id: 5,
    name: 'LEGO Star Wars R2-D2 75308 Collectible Building Toy, New 2021 (2,314 Pieces)',
    price: 249.99,
    description: 'Build and display this fantastically detailed LEGO brick model of an iconic character from the Star Wars saga: R2-D2 (75308)',
    url: 'https://m.media-amazon.com/images/I/818WPFB6+US._AC_SL1500_.jpg',
    rating: 5.0,
    amazonURL: 'https://www.amazon.com/LEGO-R2-D2-Collectible-Building-Pieces/dp/B08Z8JLGZC/ref=sr_1_9?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-9',
  },
  {
    id: 6,
    name: 'LEGO Ideas Tree House 21318 Build and Display (3036 Pieces)',
    price: 221.00,
    description: 'Challenge advanced LEGO builders and inspire role-play fun with this highly detailed LEGO Tree House, featuring 3 cabins, a tree with interchangeable summer and fall leaves and play-inspiring features including a crane, swing and a treasure chest',
    url: 'https://m.media-amazon.com/images/I/81MPRqVuZqL._AC_SL1500_.jpg',
    rating: 4.8,
    amazonURL: 'https://www.amazon.com/LEGO-6278925-Ideas-2019-3/dp/B07PX3WW5N/ref=sr_1_14?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-14',
  },
  {
    id: 7,
    name: 'LEGO Star Wars: A New Hope Mos Eisley Cantina 75290 Building Kit; Awesome Construction Model for Display, New 2021 (3,187 Pieces)',
    price: 849.99,
    description: 'Immerse yourself in a challenging build and then recreate classic Star Wars: A New Hope scenes with this highly detailed LEGO Star Wars Mos Eisley Cantina (75290) Master Builder Series display model',
    url: 'https://m.media-amazon.com/images/I/71Jl9dG1ROL._AC_SL1000_.jpg',
    rating: 4.8,
    amazonURL: 'https://www.amazon.com/LEGO-Star-Wars-Building-Construction/dp/B08HVXPWMP/ref=sr_1_19?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-19',
  },
  {
    id: 8,
    name: 'LEGO Technic Jeep Wrangler 42122; an Engaging Model Building Kit for Kids Who Love High-Performance Toy Vehicles, New 2021 (665 Pieces)',
    price: 39.99,
    description: 'With front steering, powerful axle-articulation suspension and a winch, kids can play out a world of off-roading adventures, inspired by the world-famous Jeep Wrangler',
    url: 'https://m.media-amazon.com/images/I/81VkJG9k9xL._AC_SL1500_.jpg',
    rating: 4.7,
    amazonURL: 'https://www.amazon.com/LEGO-Wrangler-Engaging-Building-High-Performance/dp/B08HVYLS6L/ref=sr_1_17?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-17',
  },
  {
    id: 9,
    name: 'LEGO Star Wars 501st Legion Clone Troopers 75280 Building Kit, Cool Action Set for Creative Play and Awesome Building; Great Gift or Special Surprise for Kids (285 Pieces)',
    price: 28.79,
    description: 'Kids can role-play as 501st Legion Clone Troopers and relive exciting action from Star Wars: The Clone Wars with this LEGO Star Wars action set (75280), featuring an AT-RT Walker and BARC Speeder',
    url: 'https://m.media-amazon.com/images/I/81iEXbFlegL._AC_SL1500_.jpg',
    rating: 4.8,
    amazonURL: 'https://www.amazon.com/LEGO-Troopers-Building-Creative-Surprise/dp/B0858LT2QL/ref=sr_1_20?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-20',
  },
  {
    id: 10,
    name: 'LEGO Technic Monster Jam Grave Digger 42118 Model Building Kit for Boys and Girls Who Love Monster Truck Toys, New 2021 (212 Pieces)',
    price: 28.00,
    description: 'Let monster truck fans recreate favorite stunts with the LEGO Technic Monster Jam Grave Digger (42118) building kit. Authentic features include huge tires, sticker details and more',
    url: 'https://m.media-amazon.com/images/I/81gMn-VVTsL._AC_SL1500_.jpg',
    rating: 4.8,
    amazonURL: 'https://www.amazon.com/LEGO-Technic-Monster-Digger-Building/dp/B08HVX5XSK/ref=sr_1_8?crid=291SIE1LY3QEM&keywords=lego&qid=1647245444&sprefix=lego%2Caps%2C443&sr=8-8',
  }

];


