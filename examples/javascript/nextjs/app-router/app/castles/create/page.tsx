import { fiefAuth } from '@/fief'

export default async function Page() {
  const accessTokenInfo = await fiefAuth.getAccessTokenInfo()

  return (
    <>
      <h2>You have the following permissions:</h2>
      <ul>
        {accessTokenInfo?.permissions.map((permission) => <li key={permission}>{permission}</li>)}
      </ul>
    </>
  )
}
