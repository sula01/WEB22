export interface Company{
  id:BigInt
  name:String
  description:String
  city:String
  address:String
  vacancy:Vacancy[]
}

export interface Vacancy{
  name:String
  description:String
  salary:BigInt
  company: BigInt
}
export interface AuthToken {
  token: string;
}
