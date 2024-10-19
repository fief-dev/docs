import { fiefAuth } from '@/fief'

export default async function Page() {
  const userInfo = await fiefAuth.getUserInfo()

  return (
    <h2>You are authenticated. Your user email is {userInfo?.email}</h2>
  )
}
